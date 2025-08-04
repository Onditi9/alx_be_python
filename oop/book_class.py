class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def _str_(self):
        return f"{self.title} by {self.author} ({self.year})"

    def _repr_(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def _eq_(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title and
            self.author == other.author and
            self.year == other.year
        )
