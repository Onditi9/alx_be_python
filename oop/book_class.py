class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def _str_(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def _del_(self):
        print(f"Deleting {self.title}")


# Optional method if needed
    def details(self):
        return f"Book '{self.title}' - {self.author} - {self.year}"
