from Utils.io.load_json import read_and_load
from Utils.decorators import singleton

@singleton
class Config:
    def __init__(self, path):
        self.config = read_and_load(path)




