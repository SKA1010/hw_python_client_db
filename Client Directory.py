import psycopg2

from pprint import pprint

 # создание таблиц
def create_db(conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40),
        surname VARCHAR(40),
        email VARCHAR(40)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phone(
        phone_number VARCHAR(11) PRIMARY KEY,
        client_id INTEGER REFERENCES client(id)
    );
    """)

def add_client(conn, first_name, last_name, email, phone=None):
    pass

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="client_directory", user="postgres", password="123") as conn:
    # вызывайте функции здесь
    with conn.cursor() as cur:
        create_db(cur)
