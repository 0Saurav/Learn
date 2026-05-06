# Mini ATM Simulator
# Concepts: functions + while loop

"""
Features:
- Balance starts at 1000
Options:
1. Check balance
2. Deposit
3. Withdraw
4. Exit
"""

print("Welcome to mini ATM simulator..")

bank_balance = 1000

def check_bal():
    global bank_balance
    print(f"Your bank balance is now {bank_balance}.")

def deposit():
    global bank_balance
    user_dep = float(input("How much you want to deposit: "))
    bank_balance += user_dep
    print(f"You deposited {user_dep}. Your bank balance is now {bank_balance}.")

def withdraw():
    global bank_balance
    user_withdraw = float(input("How much you want to withdraw? "))
    bank_balance -= user_withdraw
    print(f"You withdrew {user_withdraw}. Your bank balance is now {bank_balance}.")


inside_atm = True

while inside_atm:
    user_choice = int(input("What do you want to do \n 1 for 'check balance' \n 2 for 'deposit' \n 3 for 'withdraw' \n 4 for 'exit'. \n"))
    if user_choice == 1:
        check_bal()
    elif user_choice == 2:
        deposit()
    elif user_choice == 3:
        withdraw()
    elif user_choice == 4:
        inside_atm = False
    else:
        print("Please enter a valid choice..")
    
