"""
Name: Ethan Kidwell
py8.py

Problem: Write a program that adds 10 to each element of a list,
squares each element of a list, adds each element of a list,
converts a list of strings to number,
takes a list of strings converts them to numbers and then squares them
and adds them together,

Certification of Authenticity:
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with:
"""

import math
from graphics import GraphWin, Circle, Text, Point


def add_ten(nums):
    num_len = len(nums)
    for number in range(num_len):
        nums[number] = nums[number] + 10


def square_each(nums):
    num_len = len(nums)
    for number in range(num_len):
        nums[number] = nums[number] ** 2


def sum_list(nums):
    num_len = len(nums)
    num_total = 0
    incr = 0
    for _ in range(num_len):
        num_total = num_total + nums[incr]
        incr = incr + 1
    return num_total


def to_numbers(nums):
    incr = 0
    for num_string in nums:
        nums[incr] = float(num_string)
        incr = incr + 1


def sum_of_squares(nums):
    # accumulator for finding total of squares
    incr_3 = 0

    # this loops through the list to pull each element to edit them
    for list_element in nums:

        # this splits the numbers in the element of the list into their own elements
        num_list = list_element.split(',')

        # accumulator variables for each loop
        incr = 0  # for converting string to float
        incr_2 = 0  # for squaring each number in the list
        num_total = 0  # for looping through the list to find the total

        # Finds the length of the list to ensure it doesn't let it go out of range
        num_len = len(num_list)

        # coverts each string into a float value
        for num_string in num_list:
            num_list[incr] = float(num_string)
            incr = incr + 1

        # squares each number
        for number in range(num_len):
            num_list[number] = num_list[number] ** 2

        # totals the squared values into a single element
        for _ in range(num_len):
            num_total = num_total + num_list[incr_2]
            incr_2 = incr_2 + 1

        # sets the total value to the orginal element position in the list
        nums[incr_3] = num_total
        incr_3 = incr_3 + 1
    return nums


def starter(weight, wins):
    over_150 = weight >= 150
    under_160 = weight < 160
    over_199 = weight > 199
    win_5 = wins >= 5
    win_20 = wins > 20
    if (over_150 and win_5) and (under_160 and win_5):
        return True
    if over_199 or win_20:
        return True
    return False


def leap_year(year):
    divide_by_4 = year % 4
    divide_by_100 = year % 100
    divide_by_400 = year % 400
    if (divide_by_400 == 0) or (divide_by_100 != 0) and (divide_by_4 == 0):
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    # circle 1
    center_1 = win.getMouse()
    circumference_point = win.getMouse()
    circle_1_x = (center_1.getX() - circumference_point.getX()) ** 2
    circle_1_y = (center_1.getY() - circumference_point.getY()) ** 2
    radius = math.sqrt(( circle_1_x + circle_1_y))
    circle_one = Circle(center_1, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    # circle 2
    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    circle_2_x = (center_2.getX() - circumference_point_2.getX()) ** 2
    circle_2_y = (center_2.getY() - circumference_point_2.getY()) ** 2
    radius_2 = math.sqrt(circle_2_x + circle_2_y)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light pink")
    circle_two.draw(win)
    if did_overlap(circle_one, circle_two):
        overlapped = Text(Point(5,2), "They do overlap")
        overlapped.draw(win)
    not_overlap = Text(Point(5,2), "They do not overlap")
    not_overlap.draw(win)
    win.getMouse()


def did_overlap(circle_one, circle_two):
    circle_1_rad = circle_one.getRadius()
    circle_2_rad = circle_two.getRadius()
    circles_rad = circle_1_rad + circle_2_rad
    circle_1_center = circle_one.getCenter()
    circle_2_center = circle_two.getCenter()
    circle_1_x = circle_1_center.getX()
    circle_1_y = circle_1_center.getY()
    circle_2_x = circle_2_center.getX()
    circle_2_y = circle_2_center.getY()
    circle_distance = math.sqrt(((circle_2_x - circle_1_x) ** 2) + ((circle_2_y - circle_1_y) ** 2))
    if circle_distance <= circles_rad:
        return True
    return False


if __name__ == '__main__':
    print(leap_year(0))
