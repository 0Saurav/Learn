# Functions with Inputs

# create a function called greet() and add 3 print statements inside the function and call the greet()
def greet():
    print("Hello\n")
    print("How are you.\n")
    print("Have a great day.")

greet()

# Using a function with input

"""
def my_function(something):
    # Do this with something
    # Then do this
    # Finally do this
 
something = 'Hello'
my_function(something)

something --> parameter
123 --> argument

"""

def greet_with_name(name):
    print(f"Hello {name}.\n")
    print("Have a great day.")


greet_with_name("Saurav")

name = str(input("What is your name? "))
greet_with_name(name)    





def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")
    
age = int(input("How old are you? "))

life_in_weeks(age)

print("---------------------------")



# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You live in {location}?")

greet_with('neymar', 'brazil')  # Positional Argument
greet_with(location='argentina', name='messi') # Keyword Arguments



