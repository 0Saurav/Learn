# Prime number checker
# Goal: Loops + conditionals

"""
Task:
- Ask a number
- Check if it's prime or not

Constraint:
- Do not use advanced math
- Use loop from 2 --> n-1
"""

user_num = int(input("Enter a number: "))

is_prime = True
for num in range(2, user_num):
    if user_num % num == 0:
        is_prime = False
        break

if user_num <= 0:
    print(f"{user_num} is not greater than 1.")
elif user_num == 1:
    print(f"{user_num} not a prime.")
elif is_prime:
    print(f"{user_num} is a prime.")
else:
    print(f"{user_num} not a prime")


