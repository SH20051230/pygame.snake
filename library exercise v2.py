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

class user():
    def __init__(self, name, address):
        self.name = name # String
        self.address = address # String
        self.fees = 0.0 # Float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Fee: {self.fees}")
        print("########################")

# Print the list of users
def print_user():
    for user in user_list:
        user.user_details()

# Print the list of books
def print_info():
    for book in Book_list:
        book.book_details()

def add_user():
    name = input("What's your name?: ").title()
    address = input("where do you live?:")
    user(name, address)
    print(name, address, "has been added to the class")

def add_book():
    title = input("what the book's name: ")
    author = input("Who's the author: ")
    dewy = input("What's the book's dewy code: ")
    isbn = input("what's the book's isbn number: ")
    Book(title, author, dewy, isbn)
    print(f"{title} had been added to the book list")


def find_user():
    user_to_find = input("Please enter the user's name:").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return  user
    print("Sorry we haven't found with that name")
    return None


def found_book():
    book_to_find = input("Please enter the book's name")
    for book in Book_list:
        if book.title == book_to_find:
            print(f"The book {book_to_find} is in the catalogue")
            return book
    print("Sorry We haven't found that book")
    found_book()


def lend_book():
    user = find_user()
    print()
    if user:  # Only if user had been found
        book = found_book()  # make sure the book exist
        if book.avaliable:  # and is available
            confirm = input("Type Y to confirm if you want to borrow the book: ")
            if confirm == "Y":
                print(f"Book title {book.title} is now out"
                      f"on loan to user {user.name}")  # feedback to user
                book.available = False  # set available attribute
                book.borrower = user.name  # record the borrowed user's name
                user.borrowed_books.append(book.title)
        else:
            print(f"sorry the book {book.title} is already on loan")


def return_book():
    user = find_user()
    print()
    if user:
        book = found_book()
        if book.title in user.borrowed_book:
            confirm = input("Press Y if you want to return this book: ").upper()
            if confirm == "Y":
                print(f"Book title {book.title} is now returned"
                      f"to the library")
                book.available = True
                book.borrower = user.name
                user.borrowed_book.remove(book.title)
        else:
            print(f"Sorry {book.title} on loan to someone else")


# Main routine
Book_list = []
user_list = []

# Create the book objects
Book("Lord of the rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Book("The Hunger Game", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

user("John", "12 example St")
user("Susan", "1011 Binary Rd")
user("Paul", "25 appletree Dr")
user("Mary", "8 moon Cres")

# print user
found_book()
find_user()



print_info()

# User Menu
new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add an users")
    print("4. Add a book")
    print("5. Exit")

    choice = input("what do you want to do, type the number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Goodbye")
        new_action = False
    else:
        print("Sorry that's not a valid choice")

