import book_add
import book_fetch
import book_borrow
import book_return
import user_add
import user_fetch
import user_delete

def main():
    while True:
        choice = input('''
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Quit       
        Please enter your choice: ''')
        if choice == "1":
            book_ops()
        elif choice == "2":
            user_actions()
        elif choice == "3":
            break
        else:
            print("\nPlease enter a numeric value between 1 and 4 and try again!!!")

def book_ops():
    # print(books)
    while True:
        choice = input('''
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books   
        6. Main Menu              
        Please enter your choice: ''')
        
        if choice == "1":
            book_add.add_book()
        elif choice == "2":
            book_borrow.borrow_book()
        elif choice == "3":
            book_return.return_book()
        elif choice == "4":
            book_fetch.fetch_book()
        elif choice == "5":
            book_fetch.fetch_all_books()
        elif choice == "6":
            break
        else:
            print("\nPlease enter a numeric value between 1 and 6 and try again!!!")



def user_actions():
    while True:
        choice = input('''
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Delete a User
        5. Main Menu                     
        Please enter your choice: ''')
        if choice == "1":
            user_add.add_user()
        elif choice == "2":
            user_fetch.fetch_user()
        elif choice == "3":
            user_fetch.fetch_all_users()
        elif choice == "4":
            user_delete.delete_user()
        elif choice == "5":
            break
        else:
            print("\nPlease enter a numeric value between 1 and 4 and try again!!!")

main()