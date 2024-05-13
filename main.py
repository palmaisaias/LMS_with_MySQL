from book_add import add_book
from book_fetch import fetch_book, fetch_all_books
from user_add import add_user
from user_fetch import fetch_user, fetch_all_users
from borrow import borrow_book
from returns import return_book
import os
from colorama import Style, Fore, Back


def user_menu():

    while True:
        action = input('''
            User Operarations Menu
            ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
    
    1.) Add a new user
    2.) View user details
    3.) Display all users
    4.) Main Menu
    > ''')
        
        if action == '1':
            os.system('clear')
            add_user()
        elif action == '2':
            os.system('clear')
            fetch_user()
        elif action == '3':
            os.system('clear')
            fetch_all_users()
        elif action == '4':
            os.system('clear')
            break
        else:
            os.system('clear')
            print(Style.BRIGHT + Fore.RED+ '        Invalid Input, please try again!' + Style.RESET_ALL)

def book_menu():

    while True:
        action = input('''
            Book Operarations Menu
            ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
    
    1.) Add a new book
    2.) Search for a book
    3.) Display all books
    4.) Borrow a book
    5.) Return a book
    6.) Main Menu
    > ''')
        
        if action == '1':
            os.system('clear')
            add_book()
        elif action == '2':
            os.system('clear')
            fetch_book()
        elif action == '3':
            os.system('clear')
            fetch_all_books()
        elif action == '4':
            os.system('clear')
            borrow_book()
        elif action == '5':
            os.system('clear')
            return_book()
        elif action == '6':
            os.system('clear')
            break
        else:
            print('Invalid Input, please try again!')

while True:
    action = input('''
            Welcome to the Library Management System
            ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
                   
    Main Menu:
    1.) User Operations
    2.) Book Operations
    3.) Quit
    > ''')

    if action == '1':
        os.system('clear')
        user_menu()
    elif action == '2':
        os.system('clear')
        book_menu()
    elif action == '3':
        os.system('clear')
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '\nThank you for using Library Managenent System\n')
        break
    else:
        os.system('clear')
        print(Style.BRIGHT + Fore.RED+ '        Invalid Response, please try again'+ Style.RESET_ALL)