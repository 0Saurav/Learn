# Day 6: Python Functions, code blocks, karel, while loop

Use Reeborg's world as resource to practice about using function.
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


# turn_left() is a existing function in reebord's world

# three times turning left means turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# turning left twice means turning around
def turn_around():
    turn_left()
    turn_left()
  
# Draw a square

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


# Randomly switch at goal (Hurdle 1)
def turn_right():
    turn_left()
    turn_left()
    turn_left()


for i in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

or

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    jump()


or

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
number_of_hurdles = 6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1


# Random wall in front (Hurdle 3 in reeborg's world)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()


# Height if the wall is random (Hurdle 4)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    
# Day 6 project: Solve Maze problem in the Reeborg's world