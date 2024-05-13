from db_connection import connect_db, Error
from datetime import date

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            user_id = input('Enter the id of the user returning the book: ')
            book_id = int(input('Enter the id of the book you would like to return: '))
            return_date = date.today()

            query = ('UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL')

            cursor.execute(query, (return_date, user_id, book_id))

            available = ('UPDATE books SET availability = 1 WHERE id = %s')
            cursor.execute(available, (book_id,))

            conn.commit()
            print(f'Book returned!')

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
