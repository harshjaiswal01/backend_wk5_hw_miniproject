from db_connection import connect_db, Error
from user_fetch import fetch_all_users

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = input("What is your email? ")

            new_user = (name, email)

            query = "INSERT INTO Users (name, email) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit() #fully commits the changes
            print(f"New User {name} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


