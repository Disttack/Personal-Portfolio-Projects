def turnright():
    turn_left() # type: ignore
    turn_left() # type: ignore
    turn_left() # type: ignore

def jump():
    turn_left() # type: ignore
    move() # type: ignore
    turnright() # type: ignore
    move() # type: ignore
    turnright() # type: ignore
    move() # type: ignore
    turn_left() # type: ignore

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1