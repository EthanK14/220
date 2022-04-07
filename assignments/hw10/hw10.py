"""
Name: Ethan Kidwell
Problem: Create a program that will return a number in the fibonacci sequence based on input,



Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def fibonacci(num_seq):
    fib_list = [0, 1]  # creates the begin of the sequence
    acc = 0  # keeps track of how many times through the loop you have gone
    while not acc == num_seq:  # will stop whenever it has gone through the amount the user requested
        fib_list.append(fib_list[acc] + fib_list[acc + 1])
        acc = acc + 1
    return fib_list[num_seq]


def double_investment(principal, rate):
    pass


def syracuse(starting_value):
    # creates a list to store all values and return them
    num_list = [starting_value]
    # does the actual equation until it reaches the number 1
    acc = 0
    while num_list[acc] != 1:
        # does the even equation if starting value is even
        if num_list[acc] % 2 == 0:
            syr_even = num_list[acc] / 2

            num_list.append(syr_even)
        # does the odd equation if the starting value is odd
        else:
            syr_odd = (3 * num_list[acc]) + 1

            num_list.append(syr_odd)
        acc = acc + 1

    return num_list


def goldbach(num_list):
    pass
