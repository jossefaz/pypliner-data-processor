import logging
from Utils.Decorators.singleton import Singleton


@Singleton
class Store:

    def __init__(self):
        self.store = {}
        self.logger = logging.getLogger(__name__)

    def ger_item(self, path_string):
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
        main_key,sub_key = path
        self.store[main_key][sub_key] = value


instance = Store().instance
