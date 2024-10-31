# Library management system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Title: {self.title}, Author: {self.author}"

# Child class/derived class
class LibraryBook(Book):
    def __init__(self, title, author, isbn, copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"{self.title} is currently unavailable"

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. Copies left: {self.copies_available}"

# Usage example
book = LibraryBook("Blossoms", "George Orwell", "123456789", 18)
print(book.display())
print(book.borrow_book())
print(book.return_book())
