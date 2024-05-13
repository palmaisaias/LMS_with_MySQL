from db_connection import connect_db, Error
from colorama import Style, Fore, Back

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            full_name = input('What is the users full name: ').title()
            email = input('What is the users email: ')

            new_user = (full_name, email)

            query = "INSERT INTO users (full_name, email) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit() #---commits changes
            print(Style.BRIGHT + Fore.GREEN + "\nNew user added successfully!" + Style.RESET_ALL)
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()