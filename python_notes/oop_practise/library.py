class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.is_avialable = True


class Library:
    def __init__(self,books):
        self.books = books


    def display_books(self):
        print("Available Books: ")
        for book in self.books:
            if book.is_avialable:
                print(f"{book.title} by {book.author}")

    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.is_avialable :
                    print(f"Borrowed Book: {title}")
                    book.is_avialable = False

                else:
                    print(f"Book is not avaialable")
                break

            else:
                print("book is not avaialbe")


    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if not book.is_avialable:
                    print(f"Returned Book: {title}")
                    book.is_avialable =  True
                
                else:
                    print(f"Book is not avialble")
                break

            else:
                print("Book is not available")
                


b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Python Crash Course", "Eric Matthes")
lib = Library([b1, b2])

lib.display_books()
lib.borrow_book("Atomic Habits")
lib.display_books()
lib.return_book("Atomic Habits")
lib.display_books()


        