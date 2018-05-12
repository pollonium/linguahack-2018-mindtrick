import json

def load_data(filepath):
        file = open(filepath, 'r')
        data = file.read()

        return json.loads(data)





