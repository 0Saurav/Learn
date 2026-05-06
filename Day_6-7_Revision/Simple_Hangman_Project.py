# Hangman (Simplified Version)
# Concepts: everything till Day 6

"""
Requirements:
- Choose random word from list
- User guesses letter
- Show progress:
    _ a _ _ m a n
- Track wrong attempts (max 6)
"""
import random

word_list = ['messi', 'ronaldo', 'neymar', 'suarez']


chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)


print('\n')
guess_box = []
for i in range(0, len(chosen_word)):
    guess_box.append('_')

is_guessed = False
attempt = 6

while not is_guessed and attempt > 0:
    user_guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if user_guess == letter:
            guess_box[index] = user_guess
            
    if user_guess not in chosen_word:
        attempt -= 1
    print(f"Total attempts remaining: {attempt}")
    print(guess_box)   
    
    if guess_box == chosen_word_list:
        print(f"You got it, the word was {chosen_word}")
        is_guessed = True

if attempt == 0:
        print(f"Attempts finished, The chosen word was {chosen_word}")

