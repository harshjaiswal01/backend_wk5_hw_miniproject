from db_connection import connect_db, Error
from user_fetch import fetch_user
from book_fetch import fetch_book
from datetime import date

def borrow_book():
    conn = connect_db()
    if conn is not None:
        try:
            userid = fetch_user()
            print("USER ID : ",userid)
            bookid = fetch_book()
            print("BOOK ID : ",bookid )
            today = date.today()
            borrow_date = today.strftime("%Y/%m/%d")
            print(borrow_date)

            cursor = conn.cursor()

            borrow_update = (userid, bookid, borrow_date)
            print(borrow_update)

            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"

            cursor.execute(query, borrow_update)

            #Execute query
            conn.commit()

            cursor = conn.cursor()
            book_update = (0, bookid)

            query = "UPDATE Books SET availability = %s WHERE id = %s;" #Update query 

            cursor.execute(query, book_update)
            conn.commit()

            print(f"User {userid} has borrowed Book with ID {bookid} on {borrow_date}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()