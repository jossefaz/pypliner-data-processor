import json

def read_and_load(self, path):
    with open(path, 'r', encoding='utf-8') as jsonFile:
        return json.load(jsonFile)