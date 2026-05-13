# The Blackjack Capstone Project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_random_card():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    return user_cards, computer_cards

def calculate_score(user_cards, computer_cards):
    user_total = sum(user_cards)
    if user_total > 21 and 11 in user_cards:
        user_total -= 10
    
    computer_total = sum(computer_cards)
    if computer_total > 21 and 11 in computer_cards:
        computer_total -= 10

    return user_total, computer_total

def compare_cards(user_cards, computer_cards):
    if sum(user_cards) > sum(computer_cards):
        print(f"You won: {user_cards}")
    elif sum(computer_cards) > sum(user_cards):
        print(f"Computer won: {computer_cards}")
    else:
        print(f"It's a draw. \n Your card: {user_cards}\n Computer card: {computer_cards}")

play = str(input("Do you want to play BlackJack? Type 'y' for yes & 'n' for no: ")).lower()

if play == 'y':
    deal_random_card()
    print(user_cards)
    print(computer_cards[0], '*')
else:
    print("Ok. Let's not play then...")

game_on = True

user_total, computer_total = calculate_score(user_cards, computer_cards)
if user_total == 21 and len(user_cards) == 2:
    print("That's a Blackjack")
    print(f"You won with {user_cards}")
    game_on = False
if computer_total == 21 and len(computer_cards) == 2:
    print("That's a Blackjack")
    print(f"Computer won with {computer_cards}")


while game_on:
    another_round = str(input("Draw another card or pass? 'y' for hit & 'n' for pass: ")).lower()
    if another_round == 'y':
        user_cards.append(random.choice(cards))
        user_total, computer_total = calculate_score(user_cards, computer_cards)
        print(user_cards)
        if user_total > 21:
            print(f"You lost {user_cards}")
            game_on = False
            print(f"Computer's card {computer_cards}")  
    elif another_round == 'n':
            while computer_total < 17:
                computer_cards.append(random.choice(cards))
                user_total, computer_total = calculate_score(user_cards, computer_cards)
                print(computer_cards) 
            if computer_total > 21:
                print(f"Computer loses {computer_cards}")                              
            game_on = False
            compare_cards(user_cards, computer_cards)
                


print(user_total, computer_total)