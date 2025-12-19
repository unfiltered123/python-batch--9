class LibraryBook:

    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def add_copies(self, number):
        self.copies += number

    def issue_book(self):
        if self.copies > 0:
            self.copies -= 1
        else:
            print("No copies available")

    def return_book(self):
        self.copies += 1

    def show_details(self):
        print("\n--- Book Details ---")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Copies  :", self.copies)


book_id = input("Enter Book ID: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
copies = int(input("Enter number of copies: "))

# object creation
book1 = LibraryBook(book_id, title, author, copies)

add = int(input("Enter copies to add: "))
book1.add_copies(add)

book1.issue_book()
book1.return_book()

# show output
book1.show_details()