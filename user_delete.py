from db_connection import connect_db, Error
from user_fetch import fetch_all_users

def delete_user():
    conn = connect_db()
    if conn is not None:
        try:
            id = input("Please enter the ID of the User you want to delete: ")
            cursor = conn.cursor()
            check_query = "SELECT * FROM Users WHERE id = %s"

            cursor.execute(check_query, (id,))

            customer = cursor.fetchone()

            if not customer:
                print("User not Found! Please try Again")

            else:
            
                cursor = conn.cursor()

                query = "DELETE FROM Users WHERE id = %s"

                cursor.execute(query, (id,))
                conn.commit()
                print('Successfully Deleted User!')

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()