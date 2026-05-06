# Random Password Generator (Improved)
# Concepts: lists + loops + random

"""Requirements:
- Mix letters, numbers, symbols
- Shuffle properly
- Output as string (not list)
"""

import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


user_symbol = int(input("How many symbols do you want? "))
user_number = int(input("How many numbers do you want? "))
user_letter = int(input("How many letters do you want? "))

password_list = []
for number in range(0, user_number):
    choice = random.choice(numbers)
    password_list.append(choice)

for letter in range(0, user_letter):
    choice = random.choice(letters)
    password_list.append(choice)

for symbol in range(0, user_symbol):
    choice = random.choice(symbols)
    password_list.append(choice)


random.shuffle(password_list)

password = ''
for item in password_list:
    password += item

print(f"Your password is {password}.")
