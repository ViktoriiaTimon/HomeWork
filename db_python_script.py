import psycopg2
import os
import time

time.sleep(1)

def test_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Failed to connect: {e}")

def create_table():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS docker_users (
                id SERIAL PRIMARY KEY,
                name TEXT,
                username TEXT,
                course TEXT,
                age INT
            );
        """)
        print("Table created or already exists.")

        users = [
            ("John Doe", "john_d", "Math", 25),
            ("Alice Smith", "alice_s", "Biology", 22),
            ("Bob Johnson", "bob_j", "Physics", 30)
        ]

        cursor.executemany("""
            INSERT INTO docker_users (name, username, course, age)
            VALUES (%s, %s, %s, %s);
        """, users)

        conn.commit()
        print("Data inserted successfully!")
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Database error:", e)

def test_insert():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS docker_users (id SERIAL PRIMARY KEY, name TEXT);")
        cursor.execute("INSERT INTO docker_users (name) VALUES (%s);", ("test_name",))
        conn.commit()
        print("Insert successful!")
        conn.close()
    except psycopg2.Error as e:
        print("Database error during insert:", e)

def test_select():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM docker_users;")
        rows = cursor.fetchall()
        print(f"Data fetched: {rows}")
        conn.close()
    except psycopg2.Error as e:
        print("Database error during select:", e)
#
# def test_update():
#     conn = psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#     )
#     cursor = conn.cursor()
#     cursor.execute("UPDATE docker_users SET name = %s WHERE name = %s;", ("updated_data", "Alice Smith"))
#     conn.commit()
#     print("Update successful!")
#     cursor.execute("SELECT * FROM docker_users;")
#     rows = cursor.fetchall()
#     print(f"Data after update: {rows}")
#     conn.close()
#
# def test_delete():
#     conn = psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#     )
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM docker_users WHERE name = %s;", ("updated_data",))
#     conn.commit()
#     print("Delete successful!")
#     cursor.execute("SELECT * FROM docker_users;")
#     rows = cursor.fetchall()
#     print(f"Data after delete: {rows}")
#     conn.close()

if __name__ == "__main__":
    test_connection()
    test_insert()
    test_select()
    # time.sleep(120)
    # test_update()
    # time.sleep(120)
    # test_delete()
