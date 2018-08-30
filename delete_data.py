import sqlite3

def delete_data(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Product WHERE ProductID=?"
        cursor.execute(sql, data)

data = (2,)
delete_data(data)
