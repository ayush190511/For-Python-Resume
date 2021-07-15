class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("the books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. Please keep it safe and return it in 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("sorry this bookis either not available or has been issued to someone then please wait until the books is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning the book!")

class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book that you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book that you want to return: ")
        return self.book

if __name__=="__main__":
    centralLibrary = Library(["Algorithms", "django", "physics", "chemistry", "python"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while (True):
        WelcomeMsg = '''\n=====welcome to central library=====
        Please chooose an option:
        1. Listing all the books
        2. Request a book 
        3. Add/Return a book
        4. Exit the library'''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for choosing central library")
            exit()
        else:
            print("invalid choice")
        