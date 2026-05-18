# Name Formatter

"""
Concepts:
Functions with outputs

Task:
Ask first name and last name

Return:
John Doe

Requirements:
- use .title()
- return the formatted string
- print outside function
"""

def format_name(name):
    return name.title()

name = str(input("What is your full name? "))

print(format_name(name))
