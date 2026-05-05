# FizzBuzz (Clean Version)
# Goal: Correct logic ordering

"""
Task:
- Print 1-100
- Replace:
    - divisible by 3 --> "Fizz"
    - divisible by 5 --> "Buzz"
    - both --> "FizzBuzz
"""

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

