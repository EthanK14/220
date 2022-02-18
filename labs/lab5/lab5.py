"""
Ethan Kidwell
lab5.py

Problem: In triangle() have a user draw a triangle and them find the perimeter and area,
in color_shape() color a shape based on user giving rgb values 5 times,
in process_string() practice manipulating strings, in process_list() practice manipulating list,
in another_series() output the sum of the first elements in a repeating pattern and
print the number of terms specified by the user, in targe() draw a target using a loop.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from math import *


def triangle():
    win = GraphWin("Triangle", 600, 600)

    # prompts the user to click three times to draw the triangle
    instructions = Text(Point(300, 500), "Click three times to draw a triangle")
    instructions.draw(win)

    #  takes user input for the points for the triangle
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # gets the x and y values of the points
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()
    p3_x = p3.getX()
    p3_y = p3.getY()

    # finds the length of the different sides of the triangle
    side1_x = p2_x - p1_x
    side1_y = p2_y - p1_y
    side2_x = p2_x - p3_x
    side2_y = p2_y - p3_y
    side3_x = p3_x - p1_x
    side3_y = p3_y - p1_y
    side1_length = sqrt((side1_x ** 2) + (side1_y ** 2))
    side2_length = sqrt((side2_x ** 2) + (side2_y ** 2))
    side3_length = sqrt((side3_x ** 2) + (side3_y ** 2))

    # calculations such as perimeter and area
    perimeter = side1_length + side2_length + side3_length
    all_sides = perimeter / 2
    area = sqrt(all_sides * ((all_sides - side1_length) * (all_sides - side2_length) * (all_sides - side3_length)))

    # creates the triangle object and text objects
    user_triangle = Polygon(p1, p2, p3)
    user_triangle.setFill("light blue")
    area_display = Text(Point(300, 400), " ")
    perimeter_display = Text(Point(300, 450), " ")
    area_output = "Area:", area
    perimeter_output = "Perimeter:", perimeter
    area_display.setText(area_output)
    perimeter_display.setText(perimeter_output)

    # Draws the objects to the window
    user_triangle.draw(win)
    area_display.draw(win)
    perimeter_display.draw(win)

    # closes the window fully and manually
    instructions.setText("Click to close")
    win.getMouse()
    win.close()


def color_shape():
    """Create code to allow a user to color a shape by entering rgb amounts"""

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # entry boxes for rgb amount
    width = 5
    red_box = Entry(Point(win_width / 2, 240), width)
    green_box = Entry(Point(200, 270), width)
    blue_box = Entry(Point(200, 300), width)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    # gather rgb values
    for colors in range(5):

        # allows the user to click to enter the values
        win.getMouse()
        red_val = red_box.getText()
        green_val = green_box.getText()
        blue_val = blue_box.getText()

        # sets the values to ints to be set to rgb values
        int_red_val = int(red_val)
        int_green_val = int(green_val)
        int_blue_val = int(blue_val)

        # colors the circle
        shape.setFill(color_rgb(int_red_val, int_green_val, int_blue_val))

    # Wait for another click to exit
    click_close = "Click to Close"
    inst.setText(click_close)
    win.getMouse()
    win.close()


def process_string():
    sequences = input("Enter a string: ")
    print("First character:", sequences[0])
    print("Last character:", sequences[-1])
    print("Characters in positions 2 - 5:", sequences[1:5])
    print("Concatenations of first and last: ", sequences[1] + sequences[-1])
    print("First three 10 times: ", sequences[0:3] * 10)
    for i in sequences:
        print(i)
    print("Number of characters:", len(sequences))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1] + values[3])
    print(values[0] + values[2])
    print(values[1] * 5)
    print(values[2:5])

    float_val = float(values[5])
    list_1 = [values[2], values[3], 5]
    print(list_1)
    list_2 = [values[2], values[0], 7.2]
    print(list_2)
    print(values[2] + values[0] + float_val)
    print(len(values))


def another_series():
    seq_num = eval(input("How many terms? "))
    for seq in range(seq_num):
        print(17%3, end=" ")
        print(34%6, end=" ")
        print(78%72, end=" ")


def target():
    # creates the window
    win_length = 250
    win = GraphWin("Target", win_length, win_length)
    mid_point = Point(win_length / 2, win_length / 2)

    # creates the radius of the center circle which is the bases for all other radius's
    yellow_rad = 50 / 2

    # creating all circle object
    white_circle = Circle(mid_point, yellow_rad * 5)
    black_circle = Circle(mid_point, yellow_rad * 4)
    blue_circle = Circle(mid_point, yellow_rad * 3)
    red_circle = Circle(mid_point, yellow_rad * 2)
    yellow_circle = Circle(mid_point, yellow_rad)

    # coloring circle objects
    white_circle.setFill("white")
    black_circle.setFill("black")
    blue_circle.setFill("blue")
    red_circle.setFill("red")
    yellow_circle.setFill("yellow")

    # drawing all circle object
    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)

    # closing message and closing function
    closing = Text(mid_point,"Click to close")
    closing.draw(win)
    win.getMouse()
    win.close()