# Subscripting
print("Hello"[0])  # 'H'
print("Hello"[4])  # 'O'
print("Hello"[-1]) # 'O'

# Count starts from zero and -1 helps to get the values from behind


# Data Types

print(len('hello'))

# print(len(12345)) --> This should give TypeError


# String
print("123" + "345") # if something is inside quotes then it is a string

print("\n")
# Integer = numbers without any decimal places
num1 = 123
num2 = 345
print(num1 + num2)

print("\n")
# Large numbers
print(123_456_789) # it is for better readability for us only

print("\n")
# Float = numbers with floating values / decimal values

pi = 3.14
print(pi)


print("\n")
# Boolean values  --> True or False
print(True)
print(False)


print("\n")
# Type Error, Checking and Conversion

print('Type Error, Checking and Conversion')
# print(len(12345)) --> len() function doesnot work with integer values
print(len('12345'))

print("\n")
# Type Checking  --> use of type() function
print("Type Checking: use of type() function")

print(type(123))
print(type("saurav"))
print(type(3.14))
print(type(True))

# Type Casting / Type Conversion

print("\n")
print("Type Conversion: changing type of a variable")

print("123" + "456")

print(int("123") + int("456")) # using int(), the strings are treated as numbers.
print(type(str(123)))

float()
bool()


# print(int("abc") + int("456")) # this will give you valueError

print(type("Number of letters in your name: "))
print(type(len(input("Enter your name:"))))

print("Number of letters in your name: " + str(len(input("Enter your name:"))))



print("\n")
# Mathematical Operators:
print("Mathematical Operators: ")

print(123 + 456) # addition = +
print(7-3) # subtraction = -
print(3 * 2) # multiplication = *
print(5/3)  # division = /
print(5//3) # division that removes the floating point values

print(2**3) # exponents / power of something (2*2*2)


# PEMDAS  (PEMDAS happens from left to right)

"""
()
**
* & /
+ & -
"""

print(3 * 3 + 3 / 3 -3) # multiplication & division is prioritized at same level
# addition and subtraction are also of same level
# But the calculation goes from left to right


print(3 * (3 + 3) / 3 -3)



print("\n")
# Number Manipulation

print("Number Manipulation")

# Flooring a number --> removing all the decimal values

bmi = 71 / 1.65 ** 2
print(bmi)

print(int(bmi))

# Rounding a number --> rounding a number to nearest whhole number
print(round(bmi))

# Rounding a number with number after the dot

print(round(bmi, 2))


print("\n")
# Assignment Operator
print("Assignment Operator")

score = 0

score += 2
score -=1
score *= 2
score /= 2

print(score)



print("\n")

# Use of f-strings  --> helps to print int, str, float, bool all at once easily

score = 0 # int
height = 1.8
is_winning = True

print(f"Saurav is {height}, his score is at {score}, winning probability is {is_winning}.")