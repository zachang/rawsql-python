import sqlite3

def query(sql, data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit()

def insert_product_data(records):
    sql = "INSERT INTO Product (Name, Price, ProductTypeID) VALUES(?, ?, ?)"
    for record in records:
        query(sql, record)

def insert_product_type_data(records):
    sql = "INSERT INTO ProductType (Description) VALUES(?)"
    for record in records:
        query(sql, record)

product_types = [("sweet",), ("bitter",), ("black",)]
products = [("Green Tea", 13.9, 3), ("Cookie", 12.1, 3), ("Ginsng", 5, 2), ("Tea", 4, 2)]

insert_product_type_data(product_types)
insert_product_data(products)
