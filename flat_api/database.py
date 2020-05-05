"""This module handles connecting to a local sqlite3 database and inserting data into it.

This module is relatively simple and handles nothing more than establishing a connection
to a local sqlite3 database and inserting data into it.

  Typical usage example:

  database.insert_into_db(
           {
            'price': 500,
            'sqm': 44,
            'street': 'main street 4b',
            'area': 'NYC',
            'rooms': 5,
            'detail_view': 'www.example.com'
           }

"""
# Standard library
import _sqlite3


def insert_into_db(data):
    cursor, conn = establish_connection()
    create_db_table(cursor)
    store_in_db(cursor, conn, data)


def establish_connection():
    conn = _sqlite3.connect('flats_data.db')
    cursor = conn.cursor()

    return cursor, conn


def create_db_table(cursor):
    cursor.execute('''DROP TABLE IF EXISTS flats_data''')
    cursor.execute('''CREATE TABLE flats_data(
                            price text,
                            sqm text,
                            street text,
                            area text,
                            city text,
                            rooms text,
                            detail_view_url text
                            )
                    ''')


def store_in_db(cursor, conn, data):
    cursor.execute('''INSERT INTO flats_data VALUES (?, ?, ?, ?, ?, ?, ?)''', (
        data['price'],
        data['sqm'],
        data['street'],
        data['area'],
        data['city'],
        data['rooms'],
        data['detail_view'],
    ))
    conn.commit()
