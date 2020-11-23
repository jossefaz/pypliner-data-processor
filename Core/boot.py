from Core.Store.store import instance as store_instance
from Core.Processes.process import Process
from Tools.wrapper import Tool_wrapper
import logging

log = logging.getLogger(__name__)

def check_tools_order(process : dict) :
    if "order" not in process:
        log.error("You must provide an order list tht define the order of the processes execution in the Configuration file")
        return False
    return True

def run_pipeline(config : dict) :

    global current_process_name
    current_process_index = 0
    pipeline_success = True
    for process in config:
        pipeline_success = check_tools_order(process)
        if pipeline_success :
            current_process_name = "process_{}" + str(current_process_index), {}
            store_instance.set_item(current_process_name)
        for sub_process_name in process["order"] :
            try :
                config = process[sub_process_name]
                sub_process = Process(config)
            except KeyError as e :
                log.error(
                    "You defines a process called '{}' in the 'order' list that is not present "
                    "in the process configuration. Check the Configuration again".format(sub_process_name)
                )
                continue
            sub_process.check_and_replace(current_process_name)
            try:
                result = Tool_wrapper(sub_process.tool_name, **sub_process.arguments)
            except Exception as e:
                log.error("Error occured during the tool {}'s runtime : {}".format(sub_process.tool_name, str(e)))
                store_instance.set_item("process_{}.{}".format(str(current_process_index), sub_process_name), None)
                if sub_process.mandatory :
                    pipeline_success = False
                    break
                continue
            store_instance.set_item("process_{}.{}".format(str(current_process_index), sub_process_name), result)
        current_process_index += 1
    return pipeline_success









