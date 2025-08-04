class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def _repr_(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def _del_(self):
        print(f"Book '{self.title}' is being deleted.")