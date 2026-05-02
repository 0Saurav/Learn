# Day 4: Random modules, Lists, indexing

IndexError: list index out of range
Casues:
1. Off-by-one errors in loops: Using <= instead of < in a while loop, or using range(len(list)) when the logic actually requires range(len(list) - 1).
2. Accessing empty lists: Attempting to access my_list[0] on a list that is empty, often caused by unexpected empty inputs from APIs, files, or database queries.
3. Modifying a list while iterating: Removing or deleting items from a list while looping through it, which shrinks the list and makes previous indices invalid.
4. Hardcoded indices: Assuming a list will always have a certain number of elements, e.g., accessing my_list[5] when the list only contains 3 items.
5. Incorrect Negative Indexing: Using a negative index smaller than the length of the list, such as my_list[-5] on a 4-item list.