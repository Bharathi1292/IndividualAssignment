import csv
import json

def csv_to_json(csv_file, json_file):
    
    with open(csv_file, 'r', encoding='utf-8') as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        
        data = list(csv_reader)
    
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

csv_to_json('profiles1.csv', 'data.json')

