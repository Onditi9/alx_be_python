# main.py

from library_system import EBook, PrintBook, Library

# Create a library instance
my_library = Library()

# Create book instances
ebook1 = EBook("Digital Fortress", "Dan Brown", 5)
printbook1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 324)
ebook2 = EBook("Python 101", "Michael Driscoll", 2)
printbook2 = PrintBook("1984", "George Orwell", 268)

# Add books to the library
my_library.add_book(ebook1)
my_library.add_book(printbook1)
my_library.add_book(ebook2)
my_library.add_book(printbook2)

# List all books in the library
my_library.list_books()
