import json
stt = 'js.txt'
def load_data(filepath):
        with open(filepatch,'r') as myfile:
            return json.load(myfile)
        
def pretty_print_json(data):
        for st in data:
            print(json.dumps(st, indent="   ",ensure_ascii=False, sort_keys=True))
            
pretty_print_json(load_data(stt))        
