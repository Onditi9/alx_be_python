class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title and
            self.author == other.author and
            self.year == other.year
        )