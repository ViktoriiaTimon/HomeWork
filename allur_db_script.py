import psycopg2
import os
import allure
from allure_commons.types import Severity


@allure.step("Get DB Connection")
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


@allure.step("Table allure_users creation with user data")
def create_table_and_insert_data(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS allure_users (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    course TEXT,
                    age INT
                );
            """)
            cursor.executemany("""
                INSERT INTO allure_users (name, username, course, age)
                VALUES (%s, %s, %s, %s);
            """, [
                ("John Doe", "john_d", "Math", 25),
                ("Alice Smith", "alice_s", "Biology", 22),
                ("Bob Johnson", "bob_j", "Physics", 30),
            ])
            conn.commit()
    except Exception as e:
        allure.attach(str(e), name="Table creation error", attachment_type=allure.attachment_type.TEXT)
        raise


@allure.step("Data insert")
def insert_data(conn, name):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO allure_users (name) VALUES (%s);", (name,))
            conn.commit()
    except Exception as e:
        allure.attach(str(e), name="Insert error", attachment_type=allure.attachment_type.TEXT)
        raise


@allure.step("Data selection from allure_users")
def select_data(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM allure_users;")
            rows = cursor.fetchall()
            allure.attach(str(rows), name="Selected data", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        allure.attach(str(e), name="Selection error", attachment_type=allure.attachment_type.TEXT)
        raise

@allure.step("Data updated in the allure_users")
def test_update():
    with allure.step("Update test data in the table"):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("UPDATE allure_users SET name = %s WHERE name = %s;",
                                   ("updated_data", "Alice Smith"))
                    conn.commit()
                    print("Update successful!")
                    cursor.execute("SELECT * FROM allure_users;")
                    rows = cursor.fetchall()
                    print(f"Data after update: {rows}")
        except psycopg2.Error as e:
            allure.attach(str(e), name="Update Error", attachment_type=allure.attachment_type.TEXT)
            raise

@allure.step("Data deleted from the allure_users")
def test_delete():
    with allure.step("Delete test data in the table"):
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM allure_users WHERE name = %s;", ("updated_data",))
                    conn.commit()
                    print("Delete successful!")
                    cursor.execute("SELECT * FROM allure_users;")
                    rows = cursor.fetchall()
                    print(f"Data after delete: {rows}")
        except psycopg2.Error as e:
            allure.attach(str(e), name="Delete Error", attachment_type=allure.attachment_type.TEXT)
            raise

@allure.feature("Database Testing")
@allure.severity(Severity.CRITICAL)
def test_database_workflow():
    with allure.step("Get DB Connection"):
        conn = get_connection()

    with allure.step("Table allure_users creation with user data"):
        create_table_and_insert_data(conn)

    with allure.step("Data insert"):
        insert_data(conn, name="Test User")

    with allure.step("Data selection"):
        select_data(conn)

    with allure.step("Data updated"):
        test_update(conn)

    with allure.step("Data deleted"):
        test_delete(conn, name="updated_data")

    conn.close()
