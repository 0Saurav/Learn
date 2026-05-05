# Password Strength Checker
# Goal: Conditionals + loops

"""
Task:
- Ask for password
- Check:
    - lenght >= 8
    - contains digit
    - contains symbol (!@#$)

    Output: Weak / Medium / Strength
"""


user_pass = input("Enter a password: ")

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']



has_symbols = False
has_numbers = False
word_count = 0

for letter in user_pass:
    if letter in symbols or letter in numbers:
        has_numbers = True
        has_symbols = True
    word_count += 1

if word_count >= 8 and has_symbols and has_numbers:
    print("Your password is Strong")
elif word_count >= 8 and (has_numbers or has_symbols):
    print("Your password is Medium strength")
else:
    print("Your password is weak")
    
