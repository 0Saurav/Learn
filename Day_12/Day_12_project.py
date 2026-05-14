# Number Guessing Game
import random


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
CHOSEN_NUM = random.randint(1, 100)
print(CHOSEN_NUM)


def level(diff_level):
    if diff_level == 'easy':
        attempts = 10
    elif diff_level == 'hard':
        attempts = 5
    else:
        attempts = 0
        print("You chose wrong option")
    return attempts

def guess_again():
    if attempts <= 0:
        return ""
    else:
        print('Guess again')
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Guess again: "))
        return user_guess


diff_level = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
attempts = level(diff_level)
print(f"You have {attempts} attempts remaining to guess the number.")
user_guess = int(input("Make a guess: "))

while attempts > 0:
    if user_guess == CHOSEN_NUM:
        print("You guessed it correct. You won..")
        break
    if user_guess > CHOSEN_NUM:
        print("Too high")
        attempts -= 1
        user_guess = guess_again()
    elif user_guess < CHOSEN_NUM:
        print("Too low")
        attempts -= 1
        user_guess = guess_again()
    if attempts < 1:
        print(f"You lost. The number was {CHOSEN_NUM}")
    

