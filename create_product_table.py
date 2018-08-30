import sqlite3


def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT name from sqlite_master WHERE name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input(f"the table {table_name} already exist, do you wish to recreate(y/n)")
            if response == "y":
                keep_table = False
                print(f"the table {table_name} will be recreated and all it's data will be lost") 
                cursor.execute("DROP TABLE if exists {0}".format(table_name))
                db.commit()
            else:
                print("existing table will not be deleted")
        else:
            keep_table = False

        if not keep_table:
            cursor.execute(sql)
            db.commit()

db_name = "coffee_shop.db"

def create_product_table():
    sql = """CREATE TABLE Product(
            ProductID integer,
            Name text,
            Price real,
            ProductTypeID integer,
            primary key(ProductID),
            foreign key(ProductTypeID) references ProductType(ProductTypeID))
        """
    create_table(db_name, "Product", sql)

def create_product_type_table():
    sql = """CREATE TABLE ProductType(
            ProductTypeID integer,
            Description text,
            primary key(ProductTypeID))
        """
    create_table(db_name, "ProductType", sql)
    
create_product_type_table()
create_product_table()
