

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self._read = False  # Encapsulated attribute (starts unread)

    def read_book(self):
        self._read = True
        return f"You've are currently reading the New York Times Bestselling Book of the Month, {self.title} by {self.author}."

    def is_read(self):
        return self._read

    def summary(self):
        return f"'{self.title}' is a book by {self.author} with {self.pages} pages."

book = Book ('The Way of The Galaxy', 'Ganglittle', 20)

print (book.summary())

print(book.read_book())