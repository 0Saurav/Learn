# More on functions

"""
Functions:
def my_function():
    # Do this
    # Then do this
    # Finally do this


Functions with Inputs
def my_function(something):
    # Do this with something
    # Then do this
    # Finally do this


Functions with Outputs
def my_function():
    result = 3 * 2
    return result

output = my_function()  # the returned value will be stored in this variable
"""


# take first name and last name, and return title case
def format_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

first_name = str(input("What is your first name? "))
last_name= str(input("What is your last name? "))

full_name = format_name(first_name, last_name)

print(full_name)



output = len("Angela")

"""
len() is the function and it returns something after running the function.
"Angela" is the input.
"""



def function_1(text):
    return text + text

def function_2(text):
    return text.title()


output = function_2(function_1("hello"))

print(output)



# Multiple return values



def formatted_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return   # it returns None and ends the function early (its better to return something)
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return formatted_f_name + " " + formatted_l_name


f_name = str(input("What is your first name? "))
l_name = str(input("What is your last name? ")) 

output = formatted_name(f_name, l_name)
print(output)



# Doc_Strings: 

def doc_string_check(f_name, l_name):
    """ Takes a first and last name and format it to return the title case version of the name."""
    output = f_name + " " + l_name
    return output

output = doc_string_check('saUrav', 'SeN')
