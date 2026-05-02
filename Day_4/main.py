
# Use of random module

import random
import my_module

# Generating a random number using randint()  --> random integers

random_num1 = random.randint(0,10)  # including both end points
print(random_num1)


"""
A module is a file containing Python code
Used for reuse and organization, not just readability
"""

fav_num = my_module.my_favorite_number
print(fav_num)



# Generating a random float number

random_number_0_to_1 = random.random() * 10  # will always include zero but may never include 1 random(0,1)
print(random_number_0_to_1)


random_float_number = random.uniform(0,10) 
print(random_float_number)




print("\n")

# Python Lists: set of square brackets with data in it

print("Python Lists:")


fruits = ["Apple", "Banana", "Orange", "Peach"]
print(fruits)


print("\n")


provinces_of_nepal = ['Bagmati', 'Gandaki', 'Madhesh', 'Lumbini', 'Karnali', 'Koshi', 'Sudurpaschim']

print(provinces_of_nepal)
print(provinces_of_nepal[0])
print(provinces_of_nepal[-1]) # or print(provinces_of_nepal[6])



# Altering list
provinces_of_nepal[2] = "Madesh"
print(provinces_of_nepal)

# Adding into the list

provinces_of_nepal.append("sen")
print(provinces_of_nepal)
print(provinces_of_nepal[-1])


# Use of extend function

provinces_of_nepal.extend(["sen", "ladded"])  # adds this two to same list
print(provinces_of_nepal)

# Use of insert function

provinces_of_nepal.insert(0,'test')  # adds test to the 0 index position
print(provinces_of_nepal)


print("\n")
# Length of List

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(len(dirty_dozen[0]), len(dirty_dozen[1]))
print(len(dirty_dozen))
