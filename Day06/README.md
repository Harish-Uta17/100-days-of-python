# Escape the Maze – Reeborg's World (Python)

This project is a Python solution to the **Escape the Maze** challenge in **Reeborg's World**, an interactive environment used to learn logical thinking and Python basics.

---

## 🚀 Features
- Uses helper functions (`turn_right`, `right_is_clear`)
- Implements a right-hand wall-following algorithm
- Uses loops, conditionals, and Reeborg environment methods
- Easy to understand and beginner-friendly

---

## 🧠 Maze-Solving Logic

The robot follows the **right-hand rule**:

1. If the right side is clear → turn right and move  
2. Else if the front is clear → move forward  
3. Else → turn left  
4. Continue until reaching the goal

---

## 📌 Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def right_is_clear():
    turn_right()
    clear = front_is_clear()
    turn_left()
    return clear

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
