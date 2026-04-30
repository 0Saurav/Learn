# Tip Calculator


print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
person_count = int(input("How many person to split the bill? "))

per_person = round((total_bill + (total_bill * tip_percentage / 100)) / person_count, 2)

print(f"Each person should pay: ${per_person}")



print(f"Each person should pay: $", round((total_bill + total_bill * tip_percentage / 100) / person_count, 2))