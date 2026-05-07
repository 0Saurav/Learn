# Hangman Project 
import random


word_list = ["aardvark", "baboon", "camel"]

# TODO-1 : Randomly choose a word from the wod_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)

print(chosen_word)

# TODO-2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make it lowercase.
# TODO-2.1 : Create a "placeholder" with the same number of blanks as the chosen word

placeholder = ''

for i in range(0, len(chosen_word)):
    placeholder += '_'
print(placeholder)

lives = 6

# TODO-4 : Use a while loop to let user guess again.
game_over = False
correct_letters = []

while not game_over:
    guess = str(input("Guess a letter in the word: ")).lower()

    display = ''
# TODO-3 : Check if the letter the user guessed (guess) is one of the letters in chosen_word - print Right and Wrong accordingly.
# TODO-3.1 : Create a "display" that puts the guess letter in the right place and other as '_'.

# TODO-5 : Change the for loop so that you can keep previous correct guess
    for letter in chosen_word:
        if letter == guess:
                display += letter
                correct_letters.append(letter)
        elif letter in correct_letters: 
             display += letter  
        else:
            display += '_'
    
    if guess not in chosen_word:
        lives -= 1
        if lives  == 0:
             game_over = True
             print("You lose")

    print(f"Attempts Remaining: {lives}")

    print(display)
    if "_" not in display:
        game_over = True
        print("You won")

         

    
