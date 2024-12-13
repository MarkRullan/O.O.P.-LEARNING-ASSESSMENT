#L.A. #8
#Mark J. Rullan

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
aklat = Book("Batman", "Biboy")
libro = Book("Iron Man", "Mark")

print(aklat.title, aklat.author)
print(libro.title, libro.author)

del libro.author

print(aklat.title, aklat.author)
print(libro.title, libro.author)
