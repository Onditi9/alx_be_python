# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        "super()._init_(title, author)"
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, pages):
        "super()._init_(title, author)"
        self.pages = pages

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.pages}"
