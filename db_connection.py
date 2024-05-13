import mysql.connector #importing the mysql connector library that we pip installed
from mysql.connector import Error
from colorama import Style, Fore, Back

def connect_db():
    db_name = 'library_system' 
    user = 'root' #---MySQL user
    password = '' #---leaving this blank is the only way I could make it work
    host = 'localhost' #--localhost can be used here instead of actual digits

    #Establishing Connection
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print(Style.DIM + Fore.GREEN + "connected to MySQL Database...\n" + Style.RESET_ALL)
            return conn # Returning our connection to be used elsewhere

    except Error as e:
        print(f"Error: {e}")
        return None