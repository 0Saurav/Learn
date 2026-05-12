# Calculator Project with functions


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


n1_fresh = True
calculation_on = True
while calculation_on:
    while n1_fresh:
        n1 = float(input("What's the first number? "))
        n1_fresh = False
    operation = input("+\n-\n*\n/\n Pick an operation:")
    n2 = float(input("What's the next number? "))
    if operation in ['+', '-', '*', '/']:
        if operation == '+':
            total = add(n1, n2)
            print(f"{n1} {operation} {n2} = {total}")
        elif operation == '-':
            total = subtract(n1, n2)
            print(f"{n1} {operation} {n2} = {total}")
        elif operation == '*':
            total = multiply(n1, n2)
            print(f"{n1} {operation} {n2} = {total}")
        elif operation == '/':
            total = divide(n1, n2)
            print(f"{n1} {operation} {n2} = {total}")
    else:
        print("Invalid option")
        calculation_on = False

    choice = str(input(f"Type 'y' to continue calculating wiht {total}, or type 'n' to start a new calculaton: " ))
    if choice == 'y':
        n1 = total
        n1_fresh = False
    elif choice == 'n':
        calculation_on = True
        n1_fresh = True

