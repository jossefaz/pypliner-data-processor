import json

def read_and_load(path):
    with open(path, 'r', encoding='utf-8') as jsonFile:
        return json.load(jsonFile)