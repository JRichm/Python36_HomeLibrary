### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['Neal Shusterman', 'J. R. R. Tolkien', 'J. K. Rowling', 'James Dashner', 'Stephen King']

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append('Edgar Allan Poe')

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")

my_authors.remove('J. K. Rowling')


# Now access an element by its index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
print(my_authors[2])
# Now slice the list.

# Code here
# Example: my_authors[1:4]
slice = my_authors[0::2]
print(slice)

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
my_author_tuple = ('Neal Shusterman', 'J. R. R. Tolkien', 'J. K. Rowling', 'James Dashner', 'Stephen King')


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
my_author_set = {'Neal Shusterman', 'J. R. R. Tolkien', 'J. K. Rowling', 'James Dashner', 'Stephen King'}


# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_author_set.add('Edgar Allan Poe')

# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")

my_author_set.add('Edgar Allan Poe')
print(my_author_set)



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

print('\n')
for book in my_authors:
    print(book)

print('\n')
for book in my_author_tuple:
    print(book)

print('\n')
for book in my_author_set:
    print(book)

