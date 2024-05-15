from db_connection import connect_db, Error

def fetch_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all users
            query = "SELECT * FROM Users;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]} | Email : {row[2]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_user():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = int(input("What is the id of the User you're lookin for?"))
            cursor = conn.cursor()

            query = 'SELECT * FROM Users WHERE id = %s'

            cursor.execute(query, (user_id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]}'s Email: {row[2]}.")
        
            return user_id
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()