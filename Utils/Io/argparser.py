import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--logpath', '-lp', help="path for writting logs", type=str, default='./logs')
parser.add_argument('--logconfig', '-lc', help="path for configuring the logs file", type=str, default="Config/prod/logger.json")
parser.add_argument('--config', '-cfg', help="path of the configuration file", type=str)
parser.add_argument('--env', '-e', help="define the environment of the runtime ('DEV', 'PROD', 'TEST' are the possible values", type=str, default='DEV')
args = parser.parse_args()