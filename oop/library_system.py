class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"

    def _str_(self):
        return self.get_info()

class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def _str_(self):
        return self.get_info()

class PrintBook(Book):
    def _init_(self, title, author, page_count):
        super()._init_(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, page count: {self.page_count}"

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