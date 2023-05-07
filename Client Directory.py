import psycopg2

from pprint import pprint

# Создание таблиц
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

#Добавление данных

def add_client(cur, name=None, surname=None, email=None, phone_number=None):
    cur.execute("""
        INSERT INTO client(name, surname, email)
        VALUES (%s, %s, %s)
        """, (name, surname, email))
    cur.execute("""
        SELECT id from client
        ORDER BY id DESC
        LIMIT 1
        """)
    id = cur.fetchone()[0]
    if phone_number is not None:
        add_phone(cur, id, phone_number)

# Добавление телефона

def add_phone(cur, client_id, phone_number):
    cur.execute("""
        INSERT INTO phone(phone_number, client_id)
        VALUES (%s, %s)
        """)



def change_client(conn, id, name=None, surname=None, email=None):
    cur.execute("""
        SELECT * from client
        WHERE id = %s
        """, (id, ))
    info = cur.fetchone()
    if name is None:
        name = info[1]
    if surname is None:
        surname = info[2]
    if email is None:
        email = info[3]
    cur.execute("""
        UPDATE client
        SET name = %s, surname = %s, email =%s 
        where id = %s
        """, (name, surname, email, id))

def delete_phone(conn, id, phone_number):
    cur.execute("""
        DELETE FROM phone 
        WHERE phone_number = %s
        """, (phone_number, ))

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="client_directory", user="postgres", password="123") as conn:
    # вызывайте функции здесь
    with conn.cursor() as cur:
        #create_db(cur)
        #add_client(cur, "Алла", "Пугачёва", "IloveMaksim@yahoo.com", "8953485125")
        #add_client(cur, "Максим", "Галкин", "IloveAlla@yahoo.com", "8953485126")
        #add_client(cur, "Константин", "Кинчев", "Iloverussia@ya.ru")
        #add_client(cur, "Регина", "Дубовицкая", "regina@ya.ru", "89805476201")
        #add_client(cur, "Лев", "Лещенко", "IliveVova@gmail.com", "89202020300")
        #add_phone(cur, 6, "89204445566")
        #change_client(cur, 6, "Владимирр", "Винокур", "yayaya@ya.ru")
        #delete_phone(cur, 6, "89204445566")
