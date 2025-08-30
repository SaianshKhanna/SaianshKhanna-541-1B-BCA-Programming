class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"The book {self.title} is written by {self.author}."


class Library_record:
    
    def __init__(self):
        self.books = {} # It will be presented in {Title: Author} format


    def add_book(self, title, author): 
        
        if title.lower() in self.books:   # Checking for dupplication.
            print("This book already exists!")
        else:
            self.books[title.lower()] = author # Adds the book
            print(f"Successfully added the book, {title} by {author}.")


    def search_book(self, title):
        check_author = self.books.get(title.lower())# Checks for the given title inside the library.
        if check_author:
            print(f"Successfully founded the book, {title} by {check_author}.")
        else:
            print("No book founded with that title. Try Again.")


    def show_books(self):
        if not self.books: # Checks whether the library is empty
            print("The library is empty!")
        else:
            print("Books present in the library: ")
            for title, author in self.books.items(): # Prints out the list of books
                print(f"-'{title.title()}' by {author}")


def User():
    records = Library_record()
    
    while True:
        print("\n| ~~ MENU ~~ | \n")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. Show All Books")
        print("4. Exit")
    
        choice = input("Enter your choice [Serial No.]: ")
        #Conditional statements for working of the code as whole in one function
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the name of the author: ")
            records.add_book(title, author)

        elif choice == "2":
            title = input("Enter the title of the book: ")
            records.search_book(title)

        elif choice == "3":
            records.show_books()
            
        elif choice == "4":
            print("Exiting program...Now! \nThank you.")
            break
        
        else:
            print("Invalid input. Please, Try again!")

            
#Calling out the main function
User()
