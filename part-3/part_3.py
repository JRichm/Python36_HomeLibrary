my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project.

# Define and flesh out your function below, which should accept a dictionary as an argument when called,
# and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below


def getBookInfo(dict):
    book_string = f'The book {dict["title"]}, who was written by {dict["author"]} in the year {dict["year"]}, has {dict["pages"]} pages and a rating of {dict["rating"]}.'
    return book_string


print(getBookInfo(my_book))

# Once you are finished with that function,
# create several more functions which return individual pieces of information from the book.

# Code below


def getAuthor(dictionary):
    print(dictionary['author'])
    return dictionary['author']


def getYear(dictionary):
    print(dictionary['year'])
    return dictionary['year']


def getPages(dictionary):
    print(dictionary['pages'])
    return dictionary['pages']


def getRating(dictionary):
    print(dictionary['rating'])
    return dictionary['rating']


getAuthor(my_book)
getYear(my_book)
getPages(my_book)
getRating(my_book)


# Finally, create at least three new functions that might be useful as we expand our home library app.
# Perhaps thing of a way you could accept additional arguments when the function is called?
# Also, imagine you have a list filled with dictionaries like above.

# Code below


def setPages(dictionary, newPages):
    dictionary['pages'] = newPages
    print(dictionary['pages'])
    return dictionary['pages']


def setRating(dictionary, newRating):
    dictionary['rating'] = newRating
    print(dictionary['rating'])
    return dictionary['rating']


setPages(my_book, 391)
setRating(my_book, 4.58)
