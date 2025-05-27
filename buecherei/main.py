from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year", "publisher"])

books = [
    Book(title="1984", author="George Orwell", year=1949, publisher="Secker & Warburg"),
    Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, publisher="Lippincott"),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, publisher="Secker & Warburg"),
    Book(title="Pride and Prejudice", author="Jane Austen", year=1813, publisher="Secker & Warburg"),
    Book(title="The Picture of Dorian Gray", author="Oscar Wilde", year=1890, publisher="Lippincott"),
]
