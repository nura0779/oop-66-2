import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

connect.commit()

def create_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)
    """, (name, price, quantity))
    connect.commit()

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
    connect.commit()

update_product(1, 120)
print("после обновления: ")
print(read_products())

def delete_product(id):
    cursor.execute("""
    DELETE FROM products 
    WHERE id = ?
    """, (id,))
    connect.commit()

delete_product(2)
print("после удаления: ")
print(read_products())

create_product("Apple", 100, 10)
create_product("Banana", 150, 20)

connect.close()


