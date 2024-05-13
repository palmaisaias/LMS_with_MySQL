from db_connection import connect_db, Error
from datetime import date

def borrow_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            user_id = input('Enter the id of the user borrowing the book: ')
            book_id = int(input('Enter the id of the book you would like to borrow: '))
            borrow_date = date.today()  #---sets variable to be able to use date

            check_query = 'SELECT availability FROM books WHERE id = %s'    #---creates SQL query to pull the availability value from 'books' using the id entered by the user
            cursor.execute(check_query, (book_id,)) #--- runs the query
            availability = cursor.fetchone()    #---note that this returns a TUPLE

            if availability and availability[0] > 0:  #---I had to look this one up because I could NOT get it to work
                #---checks TWO things. First that 'availability' isnt 'None' and then checks that the value is greater than 0
                # print(availability) #---obviously this isnt necessary but it helped me see what was being kicked back from the DB

                #--- if the check of 'availability' comes back True, then program executes INSERT INTO query
                query = ('INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, NULL)')
                cursor.execute(query, (user_id, book_id, borrow_date))

                update_query = ('UPDATE books SET availability = 0 WHERE id = %s')  #---sets availability to 0
                cursor.execute(update_query, (book_id,))

                conn.commit()
                print(f'You borrowed a book!')
            else:
                print(f'\nThe book with ID {book_id} is not available for borrowing.')

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
