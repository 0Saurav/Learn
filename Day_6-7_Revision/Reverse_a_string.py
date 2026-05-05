# Reverse a String (Manual)
# Goal: Loop thinking

"""
Task:
-Input = "hello"
-Output = "olleh"
Constraint:
- Do NOT use slicing ([::-1])
"""

normal_word = str(input("Enter a word: "))

reverse_word = ''
word_count = len(normal_word) - 1

for i in range(0, word_count+1):
    reverse_word += normal_word[word_count]
    word_count -= 1


print(f"The reverse of that word is {reverse_word}.")
