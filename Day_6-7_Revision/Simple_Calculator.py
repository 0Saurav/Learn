# Simple Calculator (Functions)
# Concepts: functions + conditionals

"""Functions:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

Ask user:
- operation
- numbers
"""

print("Simple Calculator")

def add(a, b):
    sum = a + b
    return sum

def subtract(a, b):
    subtract = a - b
    return subtract

def multiply(a, b):
    multiple = a * b
    return multiple

def divide(a, b):
    division = a / b
    return division

user_choice = input("What operation do you want to do \n 1. + for 'add' \n - for 'subtract' \n * for 'multiply' \n / for 'division'.\n")
if user_choice in ['+', '-', '*', '/']:
    user_input1 = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))

    if user_choice == '+':
        total_sum = add(user_input1, user_input2)
        print(f"{user_input1} {user_choice} {user_input2} = {total_sum}")
    elif user_choice == '-':
        total_subtract = subtract(user_input1, user_input2)
        print(f"{user_input1} {user_choice} {user_input2} = {total_subtract}")
    elif user_choice == '*':
        total_multiple = multiply(user_input1, user_input2)
        print(f"{user_input1} {user_choice} {user_input2} = {total_multiple}")
    elif user_choice == '/':
        total_division = divide(user_input1, user_input2)
        print(f"{user_input1} {user_choice} {user_input2} = {total_division}")
else:
    print("Enter a valid choice.")
