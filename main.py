from Core.boot import run_pipeline
from Config.boot import Config
from Utils.Io.argparser import args

if __name__ == '__main__':
    config = Config(args.config).config
    run_pipeline(config)


