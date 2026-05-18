# Username generator

"""
Concepts:
functions + string indexing

Example:
Input:
Saurav
Sen
Output:
sausen123

Rules:
- first 3 letters of first name
- first 3 letters of last name
- add random number from 100-999
"""
import random

def username_gen(f_name, l_name):
    user_name = ''
    for i in range(0, 3):
        user_name += f_name[i]

    for i in range(0, 3):
        user_name += l_name[i]
    l_number = str(random.randint(100, 999))
    user_name += l_number

    return user_name


f_name = str(input("What is your first name? "))
l_name = str(input("What is your last name? "))

print(username_gen(f_name, l_name))
