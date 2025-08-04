# library_system.py

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def _str_(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

    def _str_(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def _init_(self, title, author, pages):
        super()._init_(title, author)
        self.pages = pages

    def _str_(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.pages}"
