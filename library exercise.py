class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()  # String with captalized letter
        self.author = author  # String
        self.dewey = dewey  # String
        self.isbn = isbn  # String
        self.avaliable = True
        self.borrower = None
        Book_list.append(self)


    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.avaliable)
        print(self.borrower)
        print("########################")


# Print the list of books
def print_info():
    for book in Book_list:
        book.book_details()


# Main routine
Book_list = []

# Create the book objects
Book("Lord of the rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Book("The Hunger Game", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

print_info()
