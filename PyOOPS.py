# Class => Library
# Layers of anstraction => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book

# Abstraction and Encapsulation


class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        print("== == == -- == == ==")
        for book in self.availableBooks:
            print(book)
        print("================================")

    def lendBook(self, requestBook):
        if requestBook in self.availableBooks:
            print("You have borrowed the book")
            self.availableBooks.remove(requestBook)
        else:
            print("Sorry, the book is not available in the Library")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank You!!!")


class Customer:
    def requestBook(self):
        print("Enter the name of book that you want to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book


library = Library(
    ['Think and grow Rich', 'Who will Cry When u dir', 'For one more day'])
customer = Customer()
while True:
    print("Enter 1: To display the available books")
    print("Enter 2: To request for a book")
    print("Enter 3: To return a book")
    print("Enter 4: To Exit")
    print("------------------------------------------")

    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
