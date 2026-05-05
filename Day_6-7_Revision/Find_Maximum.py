# Find Maximum Without max()
# Goal: Loop + comparison

"""
Task:
numbers = [34, 12, 89, 23, 67]
Find the highest value manually.
"""

numbers = [34, 12, 89, 23, 67, 91, 91.2]

max_value = 0
for number in numbers:
    if number > max_value:
        max_value = number

print(f"The maximum value in that list is {max_value}")