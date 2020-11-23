from Core.Store.store import instance
class Process:
    def __init__(self, config : dict):
        self.tool_name, \
        self.arguments, \
        self.mandatory = config.values()

    def check_and_replace(self, store_key):
        instance.check_and_replace(self.arguments, store_key)


