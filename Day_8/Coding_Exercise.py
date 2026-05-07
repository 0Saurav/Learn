# Love Calculator

def calculate_love_score(name1, name2):
    word1 = 'true'
    word2 = 'love'
    total1 = 0
    total2 = 0
    for letter in name1.lower() + name2.lower():
        if letter in word1:
            total1 += 1
        if letter in word2:
            total2 += 1
    final_total = str(total1) + str(total2)
    print(f"Love Score {final_total}")


name1 = "Kanye West"
name2 = 'Kim Kardashian'

calculate_love_score(name1, name2)
