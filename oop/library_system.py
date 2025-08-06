class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return self.get_info()

class EBook(Book):
    def __init__(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"{super().get_info()} [EBook, {self.file_size}MB]"

    def __str__(self):
        return self.get_info()

class PrintBook(Book):
    def __init__(self, title, author, weight):
        super()._init_(title, author)
        self.weight = weight

    def get_info(self):
        return f"{super().get_info()} [PrintBook, {self.weight}g]"

    def __str__(self):
        return self.get_info()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)