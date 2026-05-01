print("Welcome to Treasure Island. Your mission is to find the treasure. ")

choice1 = input("You're at intersection. Choose left or right? ").lower()
if choice1 == 'left':
    choice2 = input("Now you're in front of a river. Swimt or Wait? ").lower()
    if choice2 == 'swim':
        choice3 = input("You've now three door. Red, Blue, Yellow. ").lower()
        if choice3 == 'yellow':
            print("You win!")
        else:
            print("Game Over.")
else:
    print("Game Over..")