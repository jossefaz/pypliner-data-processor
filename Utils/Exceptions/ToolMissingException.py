class ArgumentMissingException(Exception) :

    def __init__(self, missing_tool):
        self.message = "Tool {} not found in Tools.scripts module, please check misspelling or check if this tool has its scripts in the scripts directory under Tools directory".format(missing_tool)

    def __str__(self):
        return repr(self.message)