from db_connection import connect_db, Error
from colorama import Style, Fore, Back

def fetch_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(f'Book ID: {row[0]} Title: {row[1]}, ISBN: {row[2]}, Publication Date: {row[3]}, {'Available:'+ Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Yes' + Style.RESET_ALL if row[4] else 'Available:'+ Style.BRIGHT + Fore.RED + 'No' + Style.RESET_ALL}')
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()


def fetch_book():
    conn = connect_db()
    if conn is not None:
        try:
            book_id = int(input("What is the id of the book you're lookin for? "))
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE id = %s;"

            cursor.execute(query, (book_id,))

            for row in cursor.fetchall():
                print(f'''
                      Book ID: {row[0]} 
                      Title: {row[1]}, 
                      ISBN: {row[2]}, 
                      Publication Date: {row[3]}, 
                      {'Available:'+ Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Yes' + Style.RESET_ALL if row[4] else 'Available:'+ Style.BRIGHT + Fore.RED + 'No' + Style.RESET_ALL}''')
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()