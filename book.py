class Book:
    def __init__(self,title, author, pages):
        self.title = title      
        self.author = author    
        self.pages = pages
    
    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

# Example:
b = Book("The Hobbit", "J.R.R. Tolkien", 310)
b.summary()