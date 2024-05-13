Library Management System
* This program allows you to connect to a MySQL database through python. The program allows updates to a book table a users table and incorporates a borrowed books table to manage borrowed books.
* In the main menu, you will find user operations, book operations, and the option to quit the program.
* Under user operations, you will have the option to add a new user, user details, and display all users. You will also have the option to return to the main menu.
* When adding a new user, the user will be requested to add a full name and an email. After doing so, this information will be pushed to the SQL database workbench
* View User Details will allow the user to enter the user ID and the program will kick back the name and the email of that user.
* The display all users option will show the entire table, including user ID, name and email of the users
* Book operations will allow for the user to add a new book, search for a book, display all books borrow a book and return a book.
* Add a new book, the user will be prompted for a book title, a book ISBN number, a publication date in the form of year month and day. User will receive a “book added successfully“ message.
* Search for a book will prompt the user to enter the ID of the book that they are looking for. After doing so, if the book exists in the database, the user will receive a neat output block of information, including book ID, title, ISBN number, publication date, and availability.
* Under display all books, the user will be able to see the entire list of books and the corresponding information
* If the user decides to borrow a book, the program will prompt for the ID of the user borrowing the book, as well as for the book ID of the book they would like to borrow. The program checks the availability of the book before allowing the user to borrow. If book is available, the program will print a successful message, if the book is not available, the program will notify the user stating that that specific book ID is not available to borrow
* Under return a book, the program allows any user to return any book that has been borrowed. Once the book has been returned. The program will set that books availability back to “available“
