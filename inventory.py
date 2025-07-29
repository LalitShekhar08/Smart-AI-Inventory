import json

DATA_FILE = 'data.json'

def load_inventory():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_inventory(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_inventory():
    return load_inventory()

def add_product(name, quantity, threshold):
    inventory = load_inventory()
    new_id = max([item['id'] for item in inventory], default=0) + 1
    inventory.append({"id": new_id, "name": name, "quantity": quantity, "threshold": threshold})
    save_inventory(inventory)

def update_quantity(product_id, quantity):
    inventory = load_inventory()
    for item in inventory:
        if item["id"] == product_id:
            item["quantity"] = quantity
            break
    save_inventory(inventory)
