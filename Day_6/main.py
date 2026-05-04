# Functions: a wrapper name for a block of code

print("Hello")
num_char = len("Hello")
print(num_char)

"""
Defining a function:
def my_function():
    # do this
    # then do this
    # finally do this

Calling a function:
my_function()
"""


def my_function():  # defining a function
    print("Hello")
    print("Bye")

my_function() # calling a function


# Indentations: a block of code shifted to right by four spaces
"""
def my_fucntion():
####print("Hello world")
####print("Four spaces")
    if hello == "hello":
########print("8 spaces")
"""

"""
Spaces vs Tabs
four spaces = 1 tabs 

but good practice is to have 4 spaces as per python documentation
but you cannot use tab and spaces in one same file.
"""


# While loops: a loop that goes on until a certain condition is true

"""
for item in list_of_items:
    # do something

for number in range(a,b):
    print(number)
"""

"""
while something_is_true:
    do something repeatedly
"""

number_of_hurdles = 6
while number_of_hurdles > 0:
    print(f"number of hurdles: {number_of_hurdles}")
    number_of_hurdles -= 1


"""
While loops are dangerous so need to use when you're certain.
If done badly, we might create inifinite loop.
"""
