def turn_right():
    turn_left()
    turn_left()
    turn_left()

def right_is_clear():
    # Temporarily turn right, check forward, then restore orientation.
    turn_right()
    clear = front_is_clear()
    turn_left()
    return clear

# (Optional) move forward until a wall in front, then orient left
while front_is_clear():
    move()
turn_left()

# Main maze-following loop
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
