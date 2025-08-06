class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

    def _str_(self):
        return self.get_info()

class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"{super().get_info()} [EBook, {self.file_size}MB]"

    def _str_(self):
        return self.get_info()

class PrintBook(Book):
    def _init_(self, title, author, weight):
        super()._init_(title, author)
        self.weight = weight

    def get_info(self):
        return f"{super().get_info()} [PrintBook, {self.weight}g]"

    def _str_(self):
        return self.get_info()

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)