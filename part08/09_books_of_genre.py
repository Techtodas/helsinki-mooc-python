# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------
def books_of_genre(books: list, genre: str):
    matching_books = []
    for book in books:
        if book.genre == genre:
            matching_books.append(book)
        
    return matching_books