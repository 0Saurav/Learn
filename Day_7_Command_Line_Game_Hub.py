# Command Line Game Hub 

import random

def guess_number(user_guess , chosen_number):
    if chosen_number == user_guess:
        print("You guessed it correct. \n")
        print("---------------------------")
        return True
    elif chosen_number > user_guess:
        print("You need to guess higher.")
    else:
        print("You need to guess lower.")
    return False
    


def hangman(user_guess, chosen_word, blank_field, attempts):

    for index, letter in enumerate(chosen_word):
        if user_guess == letter:
            blank_field[index] = letter
    if user_guess not in chosen_word:
        attempts -= 1
    return blank_field, attempts





    


def password_generator(nr_letters, nr_numbers, nr_symbols):
    password = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=']
    for letter in range(nr_letters):
        password += random.choice(letters)
    for symbol in range(nr_symbols):
        password += random.choice(symbols)
    for number in range(nr_numbers):
        password += random.choice(numbers)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"Your password is {password}")
    print("--------------------------------")







game_on = True

while game_on:
    user_choice = int(input("Which game do you want to play? \n 1. Play Guess the Number \n 2. Play Hangman \n 3. Password Generator \n 4. Exit \n "
    "Please enter 1, 2, 3 or 4.  "))
    if user_choice not in [1, 2, 3, 4]:
        print("PLEASE ENTER A VALID CHOICE..")
    else:
        if user_choice == 1:
            print("Playing Guess the Number.")
            game_1_finished = False
            chosen_number = random.randint(1, 50)
            while not game_1_finished:
                user_guess = int(input("Enter a number between 1 & 50: "))
                if user_guess <= 50 and user_guess >= 1:
                    game_1_finished = guess_number(user_guess, chosen_number)
                else:
                    print("PLEASE ENTER A VALID CHOICE..")
            
        elif user_choice == 2:
            print("Playing Hangman.")
            word_list = ['messi', 'neymar', 'ronaldo', 'suarez', 'aguero']
            attempts = 6
            chosen_word = random.choice(word_list)
            word_guessed = False
            blank_field = []
            for letter in range(len(chosen_word)):
                blank_field.append('_')
            while not word_guessed:    
                user_guess = str(input("Guess a letter: ")).lower()
                if user_guess in blank_field:
                    print("Already guessed. Please try another letter.")
                else:
                    blank_field, attempts = hangman(user_guess, chosen_word, blank_field, attempts)

                    blank_word = ''.join(blank_field)
                    if blank_word == chosen_word:
                        print(f"You guessed it. The word was {chosen_word}")
                        word_guessed = True
                    print(f"Attempts remaining: {attempts}")
                    if attempts == 0:
                        word_guessed = True
                        print("Attempts finished. You lose")
                        print(f"The word was {chosen_word}")
                    print(blank_word)

            

        elif user_choice == 3:
            print("Password Generator.")
            game_3_finished = False
            while not game_3_finished:
                nr_letters = int(input("How many letters would you lile in your password? \n"))
                nr_symbols = int(input("How many symbols would you like? \n"))
                nr_numbers = int(input("How many numbers would you like? \n"))
                
        else:
            print("Exiting..")
            break


