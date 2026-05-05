# Even sum calculator 
# Goal: Practice loops + conditionals

"""
Task:
- ask user for a number n
- calculate sum of all even numbers from 1 to n

Example:
Input: 10 
Output: 30 (2+4+6+8+10)

"""

print("Welcome to Even sum calculator!")

user_num = int(input("Enter a number of your choice: "))

total_sum = 0
for number in range(0, user_num+1):
    if number % 2 == 0:
        total_sum += number
        print(number)

print(f"The total sum of numbers upto {user_num} is {total_sum}.")