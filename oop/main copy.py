from library_system import Book, EBook, PrintBook, Library

book1 = Book("Pride and Prejudice", "Jane Austen")
ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
pbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

library = Library()
library.add_book(book1)
library.add_book(ebook1)
library.add_book(pbook1)

library.list_books()