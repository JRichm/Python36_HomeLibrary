### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file.
# Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def createBook():
    title = input("What is the name of the book you would like to add?\n")
    author = input("Who is the author of this book?\n")
    try:
        year = int(input("what year was this book published?\n"))
    except:
        year = int(input("Please type a number for the year?\n"))

    try:
        pages = int(input("How many pages are in this book?\n"))
    except:
        pages = int(input("Please enter a number value for amount of pages.\n"))

    try:
        rating = float(input("What is the rating of this book (1 - 5)?\n"))
    except:
        rating = float(input("Please enter a decimal value between 1 and 5.\n"))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "pages": pages,
        "rating": rating

    }

    with open('library.txt', 'a') as f:
        f.write(f'{title}, {author}, {year}, {pages}, {rating}\n')
    f.close()


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library,
# but gets the info from a list, and make it work by reading the information in your home library's .txt document.
# This will take some new logic, but you can do it.

# Code here
def getBooks():
    with open('library.txt', 'r') as f:
        file = f.readlines()

        for line in file:
            if line != None and line != '\n':

                title, author, year, pages, rating = line.split(', ')

                book_dictionary = {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "rating": float(rating),
                    "pages": int(pages)
                }
                print(book_dictionary)
    f.close()

def deleteBook(bookName):
    lineArr = []
    deleted = False
    with open('library.txt', 'r') as r:
        file = r.readlines()
        for line in file:
            lineArr.append(line)
    r.close()

    with open('library.txt', 'w') as f:
        for line in lineArr:

            if (line != '\n'):
                title, author, year, pages, rating = line.split(', ')

                if (title != bookName):
                    f.write(f'{title}, {author}, {year}, {pages}, {rating}')

                else:
                    deleted = True
                    print(f"*the book '{bookName}' has been deleted!*")

        if not deleted:
            print(f"*the book '{bookName}' could not be deleted. Please try again.*")
    f.close()



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def mainMenu():
    running = True
    while running == True:
        function = input('[V] View all books\t\t[N] Add new book\t\t[D] Delete book from list\n//')
        if (function.upper() == 'V'):
            getBooks()

        elif (function.upper() == 'N'):
            createBook()

        elif (function.upper() == 'D'):
            bookName = input('What is the name of the book you would like to delete?\n//')
            deleteBook(bookName)

        elif (function.upper() == 'X' or function.upper() == 'EXIT'):
            print('exiting...')
            running = False

        else:
            print('*no valid input*')
            mainMenu()


if (__name__ == '__main__'):
    mainMenu()