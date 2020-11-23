from Core.Store.store import instance as store_instance
from Core.Processes.process import Process
import logging

log = logging.getLogger(__name__)

def check_tools_order(process : dict) :
    if "order" not in process:
        log.error("You must provide an order list tht define the order of the processes execution in the Configuration file")
        return False
    return True

def run_pipeline(config : dict) :

    current_process_index = 0
    pipeline_success = True
    for process in config:
        pipeline_success = check_tools_order(process)
        if pipeline_success :
            store_instance.set_item("process_{}" + str(current_process_index), {})
        for sub_proccess_name in process["order"] :
            try :
                config = process[sub_proccess_name]
                sub_proccess = Process(config)
            except Exception as e :
                log.error(
                    "You defines a process called '{}' in the 'order' list that is not present "
                    "in the process configuration. Check the Configuration again".format(sub_proccess_name)
                )
                continue






