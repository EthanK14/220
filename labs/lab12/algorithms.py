"""
Name: Ethan Kidwell

Problem: Create a program that will take information from a file and
put that information into a list and then make another function
that will then take a value and see if that value is in the
list from the file.

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""


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


if __name__ == '__main__':
    # num_list = read_data('data_sorted.txt')
    # print(is_in_linear(5, num_list))
    pass
