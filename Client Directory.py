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

# Изменение клиента

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

# Удаление номера телефона

def delete_phone(conn, id, phone_number):
    cur.execute("""
        DELETE FROM phone 
        WHERE phone_number = %s
        """, (phone_number, ))

# Удаление клиента

def delete_client(conn, id):
    cur.execute("""
        DELETE FROM phone 
        WHERE client_id = %s
       """, (id,))
    cur.execute("""
        DELETE FROM client 
        WHERE id = %s
        """, (id,))    

# Поиск клиента

def find_client(conn, name=None, surname=None, email=None, phone_number=None):
    if name is None:
        name = "%"
    else:
        name = "%" + name + "%"
    if surname is None:
        surname = "%"
    else:
        surname = "%" + surname + "%"
    if email is None:
        email = "%"
    else:
        email = "%" + email + "%"
    if phone_number is None:
        cur.execute("""
            SELECT cl.id, cl.name, cl.surname, cl.email, ph.phone_number FROM client cl
            LEFT JOIN phone ph ON cl.id = ph.client_id
            WHERE cl.name LIKE %s AND cl.surname LIKE %s
            AND cl.email LIKE %s
            """, (name, surname, email))
    else:
        cur.execute("""
            SELECT cl.id, cl.name, cl.surname, cl.email, ph.phone_number FROM client cl
            LEFT JOIN phone ph ON cl.id = ph.client_id
            WHERE cl.name LIKE %s AND cl.surname LIKE %s
            AND cl.email LIKE %s AND ph.phone_number LIKE %s
            """, (name, surname, email, phone_number))
    print('Найден следующий пользователь: ', cur.fetchone())

# Вызов функции

with psycopg2.connect(database="client_directory", user="postgres", password="123") as conn:
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
        #delete_client(cur, 6)
        find_client(cur, "Максим", "Галкин")
        find_client(cur, "", "", "", "89202020300")
        find_client(cur, "", "", "Iloverussia@ya.ru",)
