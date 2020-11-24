import logging
from Utils.Decorators.singleton import Singleton


@Singleton
class Store:

    def __init__(self):
        self.store = {}
        self.logger = logging.getLogger(__name__)

    def get_item(self, path_string):
        main_key, sub_key = path_string.split('.') if isinstance(path_string, str) else path_string
        if sub_key in self.store[main_key]:
            value = self.store[main_key][sub_key]
            if value is None:
                self.logger.warning("The value retireved from store at index {} is None".format(sub_key))
            return self.store[main_key][sub_key]
        self.logger.warning(
            "The value {} passed as argument was not found in store and will thus be treated as an argument".format(
                sub_key))
        return sub_key

    def set_item(self, path_string: str, value: object):
        path = path_string.split('.')
        if path[0] not in self.store:
            self.store[path[0]] = {}
            return
        main_key, sub_key = path
        self.store[main_key][sub_key] = value

    def check_and_replace(self, argument_dict: dict, store_key):
        for arg_key, arg_value in argument_dict.items():
            if isinstance(arg_value, int) or isinstance(arg_value, str):
                existing_value = self.get_item("{}.{}".format(store_key, arg_value))
                if (isinstance(arg_value, str) or isinstance(arg_value, list)) and (
                        isinstance(existing_value, str) or isinstance(existing_value,
                                                                      list)) and arg_value == existing_value:
                    continue
                argument_dict[arg_key] = existing_value
                continue
            if isinstance(arg_value, list):
                index = 0
                for arg in arg_value:
                    if isinstance(arg, int) or isinstance(arg_value, str):
                        existing_value = self.get_item("{}.{}".format(store_key, arg_value))
                        if arg == existing_value:
                            index += 1
                            continue
                        arg_value[index] = existing_value
                        index += 1


instance = Store.instance()
