
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function: {enemies}")


# Local Scope : it exists within a function
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # it should throw name Error



# Global Scope: it exist globally like in top of the code or outside function and is accessible to everyone.

player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)


# There is no block scope in Python!

game_level = 3
enemies = ['skeleton', 'zombie', 'alien']

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# see

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) # if it is inside it will print

# if you create a variable inside a function it will be local scope
# but if you create within a block then it is not a local scope



def create_enemy():
    new_enemy = '' # this will make new_enemy to be accessed
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

print('\n')

# How to modify variables with Global Scope

enemies = 1

def increase_enemies():
    global enemies # take the variable from global scope and modify within a function
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(enemies)


# It is better not to modify a global scope within a local scope

print('\n')
enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1
   

enemies = increase_enemies(enemies)
print(enemies)


print('\n')

# Global Constants -> value you define but you never change it but to use it you can call it

PI = 3.14159 # better to keep with uppercase so that we remember not to change it in future

def my_func():
    print(PI)


my_func()