import json
import csv

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def read_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def test_csv_columns():
    data = read_csv('profiles1.csv')
    assert len(data[0]) == 12

def test_csv_rows():
    data = read_csv('profiles1.csv')
    assert len(data) >= 900

def test_json_properties():
    data = read_json('data.json')
    # Replace the below assertion with the correct one based on your JSON structure
    assert len(data) >= 900  

def test_json_rows():
    data = read_json('data.json')
    # Replace the below assertion with the correct one based on your JSON structure
    assert len(data) >= 900

def test_always_passes():
    assert True
