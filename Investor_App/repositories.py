import json
import os

JSON_FILE = 'investors_data.json'

def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_investors():
    return load_data()

def add_investor(investor):
    data = load_data()
    data.append(investor)
    save_data(data)

def delete_investor(id):
    data = load_data()
    data = [i for i in data if i['id'] != id]
    save_data(data)

def update_investor(id, updated_investor):
    data = load_data()
    for i, investor in enumerate(data):
        if investor['id'] == id:
            data[i] = updated_investor
            break
    save_data(data)


def get_investor_by_id(id):
    data = load_data()
    for investor in data:
        if investor['id'] == id:
            return investor
    return None

def generate_new_id():
    data = load_data()
    valid_entries = [investor for investor in data if 'id' in investor]
    if not valid_entries:
        return 1
    max_id = max(investor['id'] for investor in valid_entries)
    return max_id + 1