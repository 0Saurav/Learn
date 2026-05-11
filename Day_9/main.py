
# Dictionaries
"""
dictionary = {
"Key" : "Value",
"saurav" : "sen",
"lionel" : "messi"}

dictionary["saurav"]
"""


players = {
    "lionel": "messi",
    "cristiano": "ronaldo",
    "luis": "suarez"
}


print(players["cristiano"])




"""
Key        |               Value
Bug        |     An error in  a program that prevents the program from running as expected.
Function   |     A piece of code that you can easily call over and over again.
Loop       |     The action of doing something over and over again

{key: Value}

"""

programming_dictionary = {
"Bug": 'An error in  a program that prevents the program from running as expected.',
"Function": 'A piece of code that you can easily call over and over again.',
"Loop": 'The action of doing something over and over again.',
}

# Retrieving a item from the dictionaries

print(programming_dictionary["Bug"])  # Inside the square bracket you need to put key to get the value you want.

print("\n")
# print(programming_dictionary["Bog"]) # should throw KeyError

# Add a piece of data

programming_dictionary["Test"] = 'Adding one  item'

print(programming_dictionary)

print("\n")
# Wiping an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary

print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer"

print("\n")
print(programming_dictionary)


print("\n")

# Loop through a dictionary

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])




print("\n")

print("Nesting Lists and DIctionaries")

"""
{
Key: [List],
Key2: {Dict},
}
"""




capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Print Lille

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])




travel_log = {
    "France": {
        "num_types_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],

    },
    "Germany": {
        "num_types_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"],
    },
}

# Access Stuttgart

print(travel_log["Germany"]["cities_visited"][0])

# Inside travel log, inside germany, inside cities_visited, first index value

