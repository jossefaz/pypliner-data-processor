from Core.Store.store import instance
class Process:
    def __init__(self, config : dict):
        self.tool_name, \
        self.arguments = config.values()

    def check_and_replace(self):

