from db_connection import connect_db, Error
from colorama import Style, Fore, Back

def fetch_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM users;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(f'{Style.BRIGHT + 'User ID:' + Style.RESET_ALL} {row[0]} {Style.BRIGHT + 'Name:' + Style.RESET_ALL} {row[1]} {Style.BRIGHT + 'Email:' + Style.RESET_ALL} {row[2]}')
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_user():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = int(input("What is the id of the user you're lookin for? "))
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM users WHERE id = %s;"

            #Execute query
            cursor.execute(query, (user_id,))

            for row in cursor.fetchall():
                print(f'\n{Style.BRIGHT + 'User ID:' + Style.RESET_ALL} {row[0]} {Style.BRIGHT + 'Name:' + Style.RESET_ALL} {row[1]} {Style.BRIGHT + 'Email:' + Style.RESET_ALL} {row[2]}')
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()