import sqlite3





conn = sqlite3.connect('products.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image_url TEXT NOT NULL  
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def populate_products(title,description,price,image_url):
    cursor.execute('INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)',
                   (title, description, price, image_url))

# populate_products("Продукт1", "Описание продукта 1", 100,
#                   "https://balthazar.club/uploads/posts/2022-10/1666112821_37-balthazar-club-p-tort-kusok-sala-pinterest-40.png")
# populate_products("Продукт2", "Описание продуктf2", 200,
#                   "https://derevenskie-produkty-v-saratove.ru/f/store/item/82/00000282/cover/fullsize.jpg")
# populate_products("Продукт3", "Описание продукта 3", 300,
#                   "https://i.pinimg.com/736x/d6/b2/e5/d6b2e57136c343f0d0ca4d6e9eb03813.jpg")
# populate_products("Продукт4", "Описание продукта 4", 400,
#                   "https://klike.net/uploads/posts/2023-02/1675231900_4-122.jpg")


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (username, email, age))
    cursor.connection.commit()

def is_included(username):
    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    return count > 0

def check_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables
conn.commit()