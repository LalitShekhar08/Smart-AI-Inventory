import sqlite3

DB_NAME = "inventory.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            threshold INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_inventory():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    data = c.fetchall()
    conn.close()
    return data

def add_product(name, quantity, threshold):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, quantity, threshold) VALUES (?, ?, ?)", (name, quantity, threshold))
    conn.commit()
    conn.close()

def update_quantity(product_id, quantity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE inventory SET quantity=? WHERE id=?", (quantity, product_id))
    conn.commit()
    conn.close()
