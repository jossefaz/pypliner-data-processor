from Core.Store.store import instance as store_instance
class Process:
    def __init__(self, config : dict):
        self.tool_name, self.arguments = config.values()
        self.mandatory = config.values()["Mandatory"] if  "Mandatory" in config.values() else False

    def check_and_replace(self, store_key):
        store_instance.check_and_replace(self.arguments, store_key)


