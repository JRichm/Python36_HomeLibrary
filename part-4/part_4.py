### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

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


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is.
# Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "pages": pages,
        "rating": rating

    }

    print(book_dictionary)
    return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def mainMenu():
    function = input('[V] View all books\t\t[N] Add new book\t\t[D] Delete book from list\n//')
    if (function == 'V'):
        print('v')

    elif (function == 'N'):
        createBook()

    elif (function == 'D'):
        bookName = input('What is the name of the book you would like to delete?\n//')

    else:
        mainMenu()


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
while True:
    mainMenu()

