# Count Characters
# Goal: Strings + loops

"""
Task:
- Ask user for a sentence
- Count how many vowels are in it
"""
vowel = ['a', 'e', 'i', 'o', 'u']

user_sentence = str(input("Enter a sentence: ")).lower()

vowel_count = 0
for letter in vowel:
    if letter in user_sentence:
        vowel_count += 1

print(f"Vowel count: {vowel_count}")
