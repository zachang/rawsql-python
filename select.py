import sqlite3

def select_all_films():
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM film")
        result = cursor.fetchall()
        db.commit()

        return result

def select_single_film_by_year(year):
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM film WHERE releaseYear=?", (year,))
        result = cursor.fetchone()
        db.commit()

        return result

def select_all_users():
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        db.commit()

        return result

def filter_user_by_occupation(occupation: str):
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE userOccupation=?", (occupation,))
        result = cursor.fetchall()
        db.commit()

        return result

def filter_user_by_age(minAge: int, maxAge: int):
    with sqlite3.connect("movie.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE  userAge BETWEEN ? AND ? LIMIT 10", (minAge,maxAge))
        result = cursor.fetchall()
        db.commit()

        return result

users = filter_user_by_age(20, 20)
print(users)

