# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=']



print("Welcome to the PyPassword Generator! ")

nr_letters = int(input("How many letters would you lile in your password? \n"))

nr_symbols = int(input("How many symbols would you like? \n"))

nr_numbers = int(input("How many numbers would you like? \n"))


password = ''

for letter in range(nr_letters):
    password += random.choice(letters)

for symbol in range(nr_symbols):
    password += random.choice(symbols)

for number in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your password could be {password}")

password_list = list(password)
random.shuffle(password_list)


print(f"Or more secure password could be {password_list}")


