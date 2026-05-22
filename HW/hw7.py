import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

connection.commit()

def create_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)
    """, (name, price, quantity))
    connection.commit()

def read_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

print("все товары: ")
print(read_products())

def update_product(id, price):
    cursor.execute("""
    UPDATE products 
    SET price = ? 
    WHERE id = ?
    """, (price, id))
    connection.commit()

update_product(1, 120)
print("после обновления: ")
print(read_products())

def delete_product(id):
    cursor.execute("""
    DELETE FROM products 
    WHERE id = ?
    """, (id,))
    connection.commit()

delete_product(2)
print("после удаления: ")
print(read_products())

create_product("Apple", 100, 10)
create_product("Banana", 150, 20)

connection.close()