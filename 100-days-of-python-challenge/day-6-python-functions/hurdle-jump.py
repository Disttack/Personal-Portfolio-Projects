def turnright():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()

for step in range(6):
    jump()