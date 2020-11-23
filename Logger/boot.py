import os
import json
from Utils.Io.path import safe_open
from pathlib import Path
import logging
import logging.config

def setup_logging(config_path, log_path) :
    safe_open(log_path)
    if config_path is None :
        config = "../Config/prod/logger.json"
    if(Path(config_path).exists()) :
        with open(Path(config_path), 'rt') as file:
            config = json.load(file)
            for handler in config["handlers"].values():
                if "filename" in handler :
                    handler["filename"] = os.path.join(log_path, handler["filename"])
            logging.config.dictConfig(config)