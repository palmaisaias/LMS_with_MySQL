from db_connection import connect_db, Error
from book_fetch import fetch_all_books
from datetime import date

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input('What is the book title: ').title()
            isbn = input('What is the book isbn: ')
            publication_date = input('What is the publication date(YYYY-MM-DD): ')
            availability = 1

            new_book = (title, isbn, publication_date, availability)

            query = "INSERT INTO books (title, isbn, publication_date, availability) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print(f"New book added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()