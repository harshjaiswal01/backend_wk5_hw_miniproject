from db_connection import connect_db, Error
from user_fetch import fetch_user
from book_fetch import fetch_book, fetch_borrowed_books
from datetime import date


def borrow_book_id(id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all users
            query = "SELECT * FROM Borrowed_books WHERE book_id = %s;"
            bookid = (id,)
            #Execute query
            cursor.execute(query, bookid)
            borrowedid = 0

            for row in cursor.fetchall():
                # print(f"{row[0]}.) Title : {row[1]} | ISBN : {row[2]} | Author : {row[3]} | Publication Date : {row[4]} | Available : {row[5]}")
                borrowedid = row[0]
            return borrowedid
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            print("\nBooks which can be returned:-")
            fetch_borrowed_books()
            bookid = input("Please enter the ID of the book to be returned: ")
            today = date.today()
            return_date = today.strftime("%Y/%m/%d")
            borrow_id = borrow_book_id(bookid)
            print("Borrow ID: ",borrow_id)

            cursor = conn.cursor()

            borrow_update = (return_date, borrow_id)
            print(borrow_update)

            query = "UPDATE Borrowed_books SET return_date = %s WHERE id = %s"


            cursor.execute(query, borrow_update)

            #Execute query
            conn.commit()

            cursor = conn.cursor()
            book_update = (1, bookid)

            query = "UPDATE Books SET availability = %s WHERE id = %s;" #Update query 

            cursor.execute(query, book_update)
            conn.commit()

            print(f"User has returned Book with ID {bookid} on {return_date}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()