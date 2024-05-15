from db_connection import connect_db, Error

def fetch_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all users
            query = "SELECT * FROM Books;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) Title : {row[1]} | ISBN : {row[2]} | Author : {row[3]} | Publication Date : {row[4]} | Available : {row[5]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_book():
    conn = connect_db()
    if conn is not None:
        try:
            book_id = int(input("What is the id of the Book you're lookin for?"))
            cursor = conn.cursor()

            query = 'SELECT * FROM Books WHERE id = %s'

            cursor.execute(query, (book_id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]}'s")
            return book_id
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def fetch_borrowed_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all users
            query = "SELECT * FROM Books WHERE availability = 0;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) Title : {row[1]} | ISBN : {row[2]} | Author : {row[3]} | Publication Date : {row[4]} | Available : {row[5]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()