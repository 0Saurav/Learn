# Average Height (Manual)
# Goal: Lists + loops (no sum() or len())

"""
Task:
Given: 
heights = [150, 160, 170, 180]
Calculate average height manually
"""


heights = [150, 160, 170, 180]

total_height = 0
count_of_height = 0
for height in heights:
    total_height += height
    count_of_height += 1

avg_height = total_height / count_of_height
print(f"The average height is {avg_height}")