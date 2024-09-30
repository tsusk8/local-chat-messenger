import json

def get():
    with open('config.json', 'r') as file:
        return json.load(file)