"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw more squares")
    instructions.draw(win)

    # builds the orginal square
    shape = Rectangle(Point(20, 20), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to draw squares
    for i in range(num_clicks):
        click = win.getMouse()

        # Creates new parameters for the rectangle location
        change_x = click.getX()
        change_y = click.getY()
        # Creates the new squares the user draws
        new_square = Rectangle(Point(change_x, change_y), Point(change_x + 50, change_y + 50))
        new_square.setOutline("red")
        new_square.setFill("red")
        new_square.draw(win)

    # Replaces the original text for click anywhere to end and ends the program
    instructions.setText("Click anywhere to end")
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    point_acc_per = 0
    # point_acc_area = 1
    for rec in range(5):
        point = win.getMouse()
        point_x = point.getX()
        point_y = point.getY()
        point_acc_per = point_acc_per + (point_y - point_x)




def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass
