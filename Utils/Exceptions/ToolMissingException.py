class ToolMissingException(Exception) :

    def __init__(self, missing_tool):
        self.message = "Tool {} not found in Tools.executables module, please check misspelling or check if this tool has its executables in the executables directory under Tools directory".format(missing_tool)

    def __str__(self):
        return repr(self.message)