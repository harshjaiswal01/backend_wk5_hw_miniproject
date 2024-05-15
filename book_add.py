from db_connection import connect_db, Error
from book_fetch import fetch_all_books

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            print("\nPlease enter the book details to Add:")
            title = input("Title ? ").title()
            isbn = input("ISBN? ")
            author = input("Author? ").title()
            pub_date = input("Publication Date(YYYY/MM/DD)? ")


            new_book = (title, isbn, author, pub_date)

            query = "INSERT INTO Books (title, isbn, author, publication_date) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit() #fully commits the changes
            print(f"New book {title} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
