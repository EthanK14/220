"""
Name: Ethan Kidwell
Problem: Create a program that uses button.py and door.py to create a
opening and closing door.

Certificate of Authenticity:
I certify that this assignment is entirely my own work, and I disused it with: Brooks (CSL)
"""

from button import Button
from door import Door
from graphics import Rectangle, Point, GraphWin


def main():
    length = 800
    height = 700
    win = GraphWin("Door", length, height)
    win.setBackground('light grey')

    exit_rectangle = Rectangle(Point(250, 100), Point(600, 150))
    exit_button = Button(exit_rectangle, "Exit")
    exit_button.draw(win)
    door_rectangle = Rectangle(Point(250, 200), Point(600, 650))
    door_made = Door(door_rectangle, "CLOSED")
    door_made.color_door('red')
    door_made.draw(win)
    user_click = win.getMouse()
    door_state = 0
    while not exit_button.is_clicked(user_click):
        if door_made.is_clicked(user_click):
            if door_state == 0:
                door_made.undraw()
                door_made.color_door('white')
                door_made.set_label('OPEN')
                door_made.draw(win)
                door_state = 1

            elif door_state == 1:
                door_made.undraw()
                door_made.color_door('red')
                door_made.set_label('CLOSED')
                door_made.draw(win)
                door_state = 0
        user_click = win.getMouse()
    win.close()


if __name__ == '__main__':
    # main()
    pass
