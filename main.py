from connect import engine
from sqlalchemy import text

def create_table():
    with engine.connect() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                email VARCHAR(100)
            )
        """))
        print("Table created successfully.")

def insert_data():
    with engine.connect() as connection:
        data = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"}
        ]
        for user in data:
            connection.execute(
                text("INSERT INTO users (name, email) VALUES (:name, :email)"),
                user
            )
        connection.commit()  # ✅ VERY IMPORTANT: Commit after insert/update/delete
        print("Data inserted successfully.")


def read_data():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users"))
        print("Reading Data:")
        for row in result:
            print(row)

def update_data():
    with engine.connect() as connection:
        connection.execute(
            text("UPDATE users SET email = :email WHERE name = :name"),
            {"email": "newalice@example.com", "name": "Alice"}
        )
        connection.commit()  # ✅ Commit required
        print("Data updated successfully.")

def delete_data():
    with engine.connect() as connection:
        connection.execute(
            text("DELETE FROM users WHERE name = :name"),
            {"name": "Bob"}
        )
        connection.commit()  # ✅ Commit required
        print("Data deleted successfully.")

if __name__ == "__main__":
    create_table()
    insert_data()
    read_data()
    update_data()
    read_data()
    delete_data()
    read_data()
