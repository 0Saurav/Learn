# Using for loops

"""
for item in list_of_items:
    do something
"""


fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
    #print(fruits)

print(fruits)


# For loops with range() function

"""
for number in range(a, b):
    print(number)
"""



for number in range(1, 10): # from the start to the end-1
    print(number)

print("\n")

for number in range(1, 11, 3): # skip 3 steps and print number
    print(number)



# add number form 1 to 100 (The Gauss Challenge)

sum = 0
for number in range(1, 101):
    sum += number

print(sum)

