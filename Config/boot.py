from Utils.Io.load_json import read_and_load
from Utils.Decorators import singleton


class Config:
    def __init__(self, path):
        self.config = read_and_load(path)






