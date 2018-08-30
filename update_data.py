import sqlite3

def update_data(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Product SET Name=?, Price=? WHERE ProductID=?"
        cursor.execute(sql, data)
        db.commit()

data = ("Cappuccino", 3, 1)
update_data(data)