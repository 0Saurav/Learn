import random

friends = ["Messi", "Ronaldo", "Neymar", "Suarez", "Maradona", "Benzema", "Aguero"]

print("Who's going to pay the bill? ")


print(len(friends))

random_choice = random.randint(0,len(friends)-1)
payer = friends[random_choice]


print(f"{payer} is the lucky one.")


# Better way: use of random.choice()

payerr = random.choice(friends)
print(f"{payerr} is the lucky one.")
