from Core.boot import run_pipeline
from Config.boot import Config
from Utils.Io.argparser import args
from Logger.boot import setup_logging

if __name__ == '__main__':
    setup_logging(args.logconfig, args.logpath)
    config = Config(args.config).config
    run_pipeline(config)


