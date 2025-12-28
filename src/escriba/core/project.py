from escriba.core.book import Book

class Project:
    def __init__(self, name:str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book:Book):
        self.books.append(Book)