# Library-Management-System
Library Management System in Python
NEED  FOR  THE  PROJECT
In the current times, organisations  come across the  problems of arranging bulk information in a way that it’s easy to access and update.
This project will help in solving such a problem faced by a school/public library to a great extent.
The project introduces and implements the concept of file handling as well as user-defined functions in Python.
This project helps you keeping track of the details of books present in the library as well as the people’s details who own a membership there.
PACKAGES AND DATA STRUCTURE

1. Packages used:
CSV
os
2. Data structure used:
List
FUNCTIONS DESCRIPTION

1. Add_books( )- To add book’s data
2. membership( )-To register, cancel or update membership
3. Issue_book( )-To accept book id and member id from the user and check whether that particular book is already issued or not and it also verifies whether that member has already issued a book or not. If the conditions are false then it successfully issues the book whose book id is accepted from the user 
4. Return_Book()-It accepts member id from the user and verifies whether that particular member has issued any book or not. If the member has issued a book, it accepts the number of days since the book was with the member, date of issue, book id, member id, and member name. If the number of days exceed 14, then it will charge the fine according to the number of days the member has kept the book, following the rules of the library and the book will be finally returned.
5. search_record()- To search and print records of a particular book or a member according to the choice accepted by the user.
6. display_record()-To display the records of all books and members in the library according to the choice accepted by the user.

