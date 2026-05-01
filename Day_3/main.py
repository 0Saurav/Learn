# Control flow with if / else and conditional operators

"""
if condition:
    do this
else:
    do this
"""



print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You're eligible to ride rollercoaster.")
else: 
    print("Sorry you cannot join us.")


# if height > 120:
# print("Indentation Error")  # This will cause indentation error



print("\n")

if height == 120:
    print("You can ride rollercoaster still")
else:
    print("You cannot ride")

# Use of double equals to == means actual equals to
# Use of single equals to = means assignment of a values


# Modulo Operator: give back the remainder in a division operation
print("\n")
print("Modulo Operator")


print(10 % 5)
print(10 % 3)



# Check ODD or EVEN

user_num = int(input("Enter a number: "))

if user_num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n")

# Nested if else : using if/else inside a if else statements
print("Nested IF / ELSE")

"""
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket price is $5.")
    elif age <= 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else: 
    print("You're out")




print("\n")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")


# Logical Operators: use of and , or , not.
print("\n")
print("Logical Operators")


# A and B --> both needs to be true
# A or B --> one of them needs to be true
# not A --> opposite of what A is, if true then its false and vice versa.


