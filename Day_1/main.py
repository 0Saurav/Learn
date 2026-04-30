# Write your code below this line

# Use of print statements
print("Use of print function")
print("Hello World")

# print("Hello world)  --> this will cause syntax error

print("\n")
print("String Manipulation")
# The pieces of characters inside " " is called string.
# String Manipulaition

print("Hello World!\nHello World!")

# Backslash n --> \n help to escape one line

# String Concatenation
print("\n")
print("String Concatenation")

print("Hello" + "Saurav")  # this will combine both string without any space characters

# To add a space between those strings

print("Hello " + "Saurav") # add space at last of first string
print("Hello" + " Saurav") # add space at first of second string
print("Hello" + " " + "Saurav") # add space as one string itself

# print("Saurav")  --> it will cause indentation error

print("\n")

# Use of input() function 

input("What is your name?")  # this will ask input but cannot store the value on any something

print("Hello " + input("What is your name?") + "!") # it will print the inputed value directly


# Comments

# Use of hashtag # --> it will be written in code but not executed (used for single line comments)
"""
Important Clarification:
- Triple quotes are actually multi-line strings, not true comments
- Python just ignores them if unused
"""


print("\n")

# Variables  --> naming something so that it can be used to store value like a container and later can be called easily
print("Variables")


name = input("What is your name? ") # name will store what the user types in as input
print("Hello", name)



name = "John Cena"  # now name holds John Cena not the user input
print(name)

name = "Batista" # now name hold Batista not John Cena
print(name)



# Use of len() function
print("\n")

print("Use of len() function")
username = input("What is your name?")
word_length = len(username)

print("Your name", username, "has", word_length, "characters in it.")

# len() it helps to count the number of characters a string has | length of a string

"""

name = 'sen'
length = len(nes) # this will cause a NameError

print(length)

"""