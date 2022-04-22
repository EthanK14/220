"""
Name: Ethan Kidwell

Problem: Create a program that will take information from a file and
put that information into a list and then make another function
that will then take a value and see if that value is in the
list from the file.

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""

from graphics import Rectangle, Point

def read_data(file_name):
    num_file = open(file_name, 'r')  # opens the file for reading
    num_read = num_file.read()  # gets the entire contents of file
    num_no_line = num_read.replace('\n', ' ')  # removes all new line characters from the file
    string_list = num_no_line.split(' ')  # splits the numbers in the file into a list on spaces
    acc = 0  # accumulator to keep track in while loop and indexing
    num_list = []  # new list of nums to be returned
    while acc < len(string_list):  # loop that loops through the list
        num_list.append(eval(string_list[acc]))  # adds # to the list
        acc += 1  # accumulates
    num_file.close()
    return num_list


def is_in_linear(search_val, num_list):
    list_len = len(num_list)  # gets the len of list for loop
    acc = 0  # accumulator to keep loop in scope
    while acc < list_len:  # while acc less than the length of the list
        if num_list[acc] == search_val:
            # if searched value is in list return true else accumulate to look at next value
            return True
        else:
            acc += 1
    return False  # if not in list return false


def is_in_binary(search_val, values):
    values.sort()
    left_index = 0
    right_index = len(values) - 1
    # step 2
    while left_index <= right_index:
        middle_index = (right_index + left_index) // 2
        middle_value = values[middle_index]
        if middle_value == search_val:
            return middle_index
        elif middle_value < search_val:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1


def selection_sort(nums):
    n = len(nums)
    for bottom in range(n - 1):
        mp = bottom
        for i in range(bottom + 1, n):
            if nums[i] < nums[mp]:
                mp = i
        nums[bottom], nums[mp] = nums[mp], nums[bottom]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()
    side_1 = abs(p1_x - p2_x)
    side_2 = abs(p1_y - p2_y)
    area = side_1 * side_2
    return area


def rect_sort(rectangles):
    rect_len = len(rectangles)
    for bottom in range(rect_len - 1):
        mp = bottom
        for i in range(bottom + 1, rect_len):
            if calc_area(rectangles[i]) < calc_area(rectangles[mp]):
                mp = i
        rectangles[bottom], rectangles[mp] = rectangles[mp], rectangles[bottom]



if __name__ == '__main__':
    # num_list = read_data('test.txt')
    # # print(is_in_linear(5, num_list))
    # rect_big = Rectangle(Point(100, 100), Point(250, 300))
    # rect_small = Rectangle(Point(50, 50), Point(10, 10))
    # rect_mid = Rectangle(Point(100, 100), Point(150, 200))
    # print(calc_area(rect_small))
    # print(calc_area(rect_mid))
    # print(calc_area(rect_big))
    # rect_list = [rect_big, rect_small, rect_mid]
    # rect_sort(rect_list)
    # print(rect_list)
    pass
