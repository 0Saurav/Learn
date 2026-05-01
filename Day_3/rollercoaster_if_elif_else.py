"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    else:
        bill += 12
        print("Adult tickets are $12.")
    photo_choice = input("Do you want your photo taken? 'y' for Yes or 'n' for No. ").lower()
    if photo_choice == 'y':
        # adding 3 in total bill
        bill += 3
    else:
        bill = bill
    print(f"Your total bill will be ${bill}.")
else: 
    print("You're not eligible to join us.")

"""




print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        bill += 0
        print("For you tickets on us.")
    elif age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    else:
        bill += 12
        print("Adult tickets are $12.")
    photo_choice = input("Do you want your photo taken? 'y' for Yes or 'n' for No. ").lower()
    if photo_choice == 'y':
        # adding 3 in total bill
        bill += 3
    else:
        bill = bill
    print(f"Your total bill will be ${bill}.")
else: 
    print("You're not eligible to join us.")
