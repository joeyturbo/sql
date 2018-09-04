import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
    ('Ford','F-150',1),
    ('Ford','Mustang',1),
    ('Ford','Explorer',1),
    ('Honda','Del Sol',1),
    ('Honda','Passport',1)
    ]

    c.executemany('INSERT INTO inventory VALUES(?,?,?)',cars)

    c.execute('SELECT * FROM inventory')

    rows = c.fetchall()

    for r in rows:
        print(r[0],r[1],r[2])
