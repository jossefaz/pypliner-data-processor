from Utils.Exceptions.ArgumentMissingException import ArgumentMissingException
from Utils.Exceptions.ToolMissingException import ToolMissingException
from Utils.Sanity.check_func_args import check_func_args
from importlib import import_module
import logging
from Utils.Io.argparser import args
import inspect


class Tool_wrapper:

    def __init__(self, tool_name, **tool_params):
        self.logger = logging.getLogger(__name__)
        self.tool_name = tool_name
        self.tool = self.init_tool(tool_name)
        self.parameters = tool_params

    def init_tool(self, tool_name):
        if not args.env or args.env not in ["DEV", "PROD", "TEST"]:
            self.logger.error("You must provide an environment argument to run this script '--env DEV' for example")
            raise ArgumentMissingException("--env")
        try:
            return import_module("Tools.executables.{}.{}".format(args.env.lower(), tool_name))
        except Exception as e:
            self.logger.error(str(e))
            raise ToolMissingException(tool_name)

    def execute_tool(self):
        main_function = getattr(self.tool, "main")
        arguments = inspect.getfullargspec(main_function)
        checked_args = check_func_args(arguments[0], self.parameters)
        if len(checked_args) == 0:
            return main_function(**self.parameters)
        arguments_literals = ', '.join(checked_args)
        self.logger.error(
            "In the tool {} some mandatory arguments were not found in the configuration file : {}".format(
                self.tool_name, arguments_literals))
        raise ArgumentMissingException(arguments_literals)
