import _sqlite3


def insert_into_db(data):
    cursor, conn = establish_connection()
    create_db_table(cursor)
    store_in_db(cursor, conn, data)


def establish_connection():
    conn = _sqlite3.connect('test_data.db')
    cursor = conn.cursor()

    return cursor, conn


def create_db_table(cursor):
    cursor.execute('''DROP TABLE IF EXISTS flat_data''')
    cursor.execute('''CREATE TABLE flat_data(
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
    cursor.execute('''INSERT INTO flat_data VALUES (?, ?, ?, ?, ?, ?, ?)''', (
        data['price'],
        data['sqm'],
        data['street'],
        data['area'],
        data['city'],
        data['rooms'],
        data['detail_view'],
    ))
    conn.commit()
