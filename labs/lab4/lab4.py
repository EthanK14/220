"""
Ethan Kidwell
lab4.py

Problem: Make a valentines' day card that displays a message and has an arrow go through a heart.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def greeting_card():
    # Creates the window for the card and set color
    win = GraphWin("Valentines Day Card <3", 500, 600)
    win.setBackground("pink")
    # Creates text object for the card
    valentines_text = Text(Point(250, 50), "<3 HAPPY VALENTINES DAY <3")

    # Reused points for the different shapes
    middle_point = 225  # Controls the height of the heart as a whole
    end_point = middle_point + 150  # Saves the y coordinate for the bottom in relation to the middle point
    circle_1_centers = Point(210, middle_point)
    circle_2_center = Point(290, middle_point)

    # Creates all the different shapes for the heart to be made
    # Creates the first circle for the heart
    circle_1 = Circle(circle_1_centers, 50)
    circle_1.setFill("red")
    circle_1.setOutline("red")

    # Creates the second circle
    circle_2 = Circle(circle_2_center, 50)
    circle_2.setFill("red")
    circle_2.setOutline("red")

    # Creates the triangle to tie the heart together
    triangle = Polygon(Point(175, middle_point), Point(325, middle_point), Point(250, end_point))
    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.setWidth(35)

    # Creates the location for the click to exit message
    end_text = Text(Point(250, 550), "")

    # Where the arrow is created
    arrow_shaft = Rectangle(Point(0, 400), Point(210, 408))
    arrow_shaft.setFill("black")
    arrow_head = Polygon(Point(200, 410), Point(200, 398), Point(225, 404))
    arrow_head.setFill("black")

    # Where everything is drawn to the window
    arrow_shaft.draw(win)
    arrow_head.draw(win)
    valentines_text.draw(win)
    circle_1.draw(win)
    circle_2.draw(win)
    triangle.draw(win)
    end_text.draw(win)

    # Arrow Animation
    for arrow in range(9):
        time.sleep(.5)
        arrow_shaft.move(15, -10)
        arrow_head.move(15, -10)

    # Displays the click to end text
    end_text.setText("Click Anywhere to End")
    win.getMouse()
