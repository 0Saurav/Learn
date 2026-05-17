def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()

# Desribe the problem  - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

""" The range function will work from 1 to till 20 that is n-1 = 19.
The for loop is iterating each value in range of 1 to 20.
If i is equals to 20 then it should print "You got it"
The value of i will start from 1 to till 19 only so there will be no i == 20
"""
def my_function():
    for i in range(1, 21): # Instead of 20 it should be 21
        if i == 20:
            print("You got it")

my_function()



print("--------------------------------------")

from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_images[dice_num]) # sometimes will throw error
"""
Traceback (most recent call last):
  File "e:\Learn\Day_13\main.py", line 33, in <module>
    print(dice_images[dice_num])
          ~~~~~~~~~~~^^^^^^^^^^
IndexError: list index out of range
"""

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice_num)

# In this case randint will return numbers from 1 to 6 including both end points
# But the list has 6 characters with index 0 t0 5, when randint gives 6 program will return error

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)  # make it 0 t0 5 so that all index is included
print(dice_num)
print(dice_images[dice_num])


print("--------------------------------------")


year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a mllenial.")
elif year > 1994:
    print("You're a Gen Z")

# This will not take 1994 as millenial or as a Gen Z.

"""
year = 1994
if True and False:
    this will be false
elif False:
    this will be false    
"""
# There is no bucket to catch 1994 in those mentioned conditions.

if year > 1980 and year < 1994:
    print("You are a mllenial.")
elif year >= 1994:
    print("You're a Gen Z") # Adding equals to along with greater than symbol it should include 1994 also now.

print("--------------------------------------")

"""
age = int(input("How old are you? "))
if age > 18:
print("You can drive at age {age}.")
"""
# This block of code will have many error and normally code editor will throu those error instantly.
# Always fix it when its shown immediately

age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")


# Try and Except way

try: 
    age = int(input("How old are you? "))
except ValueError:
    print("Thats a invalid type. Please enter a numerical value like 15")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")

print("--------------------------------------")


word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page  

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)


word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # there's double equals to sign being used
total_words = pages * word_per_page  

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)
