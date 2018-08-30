import sqlite3

def insert_data(values):
    with  sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "INSERT INTO Product (Name, Price) VALUES (?, ?)"
        cursor.execute(sql, values)
        db.commit()

product = ("Expresso", 2.0)
insert_data(product)

