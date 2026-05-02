# Rock, Paper and Scissors
import random



# Rock Paper Scissors ASCII Art

# Rock
gesture = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" , 
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]



print("Let's play Rock, Papers or Scissors..")

computer_choice = random.randint(0,2)


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))




if user_choice > 2 or user_choice < 0:
    print("Invalid choice. Its just 0 1 2")
elif user_choice == 0 and computer_choice == 2:
    print(f"Computer chose: \n{gesture[computer_choice]}")
    print(f"You chose: \n{gesture[user_choice]}")
    print("You won")
elif user_choice == 1 and computer_choice == 0:
    print(f"Computer chose: \n{gesture[computer_choice]}")
    print(f"You chose: \n{gesture[user_choice]}")
    print("You won")
elif user_choice == 2 and computer_choice == 1:
    print(f"Computer chose: \n{gesture[computer_choice]}")
    print(f"You chose: \n{gesture[user_choice]}")
    print("You won")
elif user_choice == computer_choice:
    print(f"Computer chose: \n{gesture[computer_choice]}")
    print(f"You chose: \n{gesture[user_choice]}")
    print("It's a draw")
else:
    print(f"Computer chose: \n{gesture[computer_choice]}")
    print(f"You chose: \n{gesture[user_choice]}")
    print("You lost!")




