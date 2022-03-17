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
import graphics


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
    for i in range(num_len):
        num_total = num_total + nums[incr]
        incr = incr + 1
    return num_total


def to_numbers(nums):
    incr = 0
    for num_string in nums:
        nums[incr] = float(num_string)
        incr = incr + 1


# nums = ['1, 2, 3', '4, 5, 6']

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
        for i in range(num_len):
            num_total = num_total + num_list[incr_2]
            incr_2 = incr_2 + 1

        # sets the total value to the orginal element position in the list
        nums[incr_3] = num_total
        incr_3 = incr_3 + 1
    return nums


def starter(weight, wins):
    pass


def leap_year(year):
    pass


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass
