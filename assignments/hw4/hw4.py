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
import math


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
    # point_acc_per = 0
    # # point_acc_area = 1
    # Creating objects for the windows
    point_1 = win.getMouse()
    point_x = point_1.getX()
    point_y = point_1.getY()
    point_2 = win.getMouse()
    point_x_2 = point_2.getX()
    point_y_2 = point_2.getY()
    long_square = Rectangle(Point(point_x, point_y), Point(point_x_2, point_y_2))
    perimeter_text = Text(Point(200, 300), " ")
    area_text = Text(Point(200, 325), " ")

    # calculations for area and perimeter
    side_1 = (point_x_2 - point_x)  # gets side length
    side_2 = (point_y_2 - point_y)  # gets side length off the same point as the first length ensuring a different side
    perimeter = (side_1 * 2) + (side_2 * 2)
    area = side_1 * side_2

    # Drawing all objects to the windows
    long_square.setFill("light blue")
    long_square.draw(win)
    perimeter_text.draw(win)
    area_text.draw(win)

    # Setting the text to the widow from calculations
    perimeter_value = "Perimeter:", perimeter
    area_value = "Area:", area
    perimeter_text.setText(perimeter_value)
    area_text.setText(area_value)

    # closes the program
    close_prompt = Text(Point(200, 380), "Click to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)

    # Create the circle
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    p_1_x = point_1.getX()
    p_1_y = point_1.getY()
    p_2_x = point_2.getX()
    p_2_y = point_2.getY()
    middle_point = Point(p_1_x, p_1_y)
    half_diameter = p_2_x - p_1_x
    # Calculations of the circle
    x_values = (p_2_x - p_1_x) ** 2
    y_values = (p_2_y - p_1_y) ** 2
    radius = math.sqrt(x_values + y_values)
    round_thing = Circle(middle_point, radius)

    # prints the radius to the screen
    radius_words = "Radius:", radius
    true_radius = Text(Point(200, 350), " ")
    true_radius.setText(radius_words)

    # Drawing everything to the window
    round_thing.draw(win)
    true_radius.draw(win)
    # closes the program
    close_prompt = Text(Point(200, 380), "Click to close")
    close_prompt.draw(win)
    win.getMouse()
    win.close()


def pi2():
    # number of terms the user wants
    num_terms = eval(input("Enter the number of terms to sum: "))
    pi_approx = 0
    denominator = 1
    change = 1
    # Loop to calculate approximation
    for i in range(1, num_terms + 2, 2):
        pi_approx = pi_approx + (change * (4 / denominator))
        denominator = denominator + 2
        change = change * - 1

    # gets accuracy from difference of true pi
    accuracy = (pi_approx - math.pi)

    # Prints results
    print("Pi approximation: ", pi_approx)
    print("Approximation was ", accuracy, "away from true pi")



if __name__ == '__main__':
    pass
