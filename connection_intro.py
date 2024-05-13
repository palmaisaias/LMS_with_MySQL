import mysql.connector 
from mysql.connector import Error

# Database connection Parameters
db_name = 'library_system' 
user = 'root' #---MySQL user
password = '' #---no password is dependant on user interface
host = 'localhost' #--localhost can be sued here instead of digits

try:
    conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host
    )

    cursor = conn.cursor() #---'middle-man' between pyhton and MySQL

    query = "SELECT * FROM users;"

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    if conn.is_connected():
        print("Connected to MySQL Database")

except Error as e:
    print(f"Error: {e}")
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close() #---close connection
        print("MySQL Connection Closed")