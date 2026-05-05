# Guess the Number (Basic)
# Goal: While Loop

"""
Task:
- Generate random number (1-50)
- Keep asking user until correct
"""

import random


chosen_number = random.randint(1,50)

is_guess = False

while not is_guess:
    user_guess = int(input("Guess the number(1-50): "))
    if user_guess == chosen_number:
        print(f"Correct, The number was indeed {user_guess}")
        is_guess = True


