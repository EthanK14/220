"""
Name: Ethan Kidwell
Problem: Create a program that will return a number in the fibonacci sequence based on input,

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import GraphWin, Point
from face import Face

def fibonacci(num_seq):
    fib_list = [0, 1]  # creates the begin of the sequence
    acc = 0  # keeps track of how many times through the loop you have gone
    while not acc == num_seq:  # will stop whenever it has gone through the amount the user requested
        fib_list.append(fib_list[acc] + fib_list[acc + 1])
        acc = acc + 1
    return fib_list[num_seq]


def annual_rate(principal, rate):
    annually_rate = principal * (1 + rate)
    return annually_rate


def double_investment(principal, rate):
    annually_rate = 0
    number_years = 0
    double_principal = principal * 2
    while not double_principal <= annually_rate:
        number_years = number_years + 1
        annually_rate += annual_rate(principal, rate)
        print(double_principal)
        print(annually_rate)
    return number_years


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


def is_prime(num):
    if num % 1 == 0 and num % num == 0:
        return True
    return False


def get_prime_num(num):
    prime_list = [2]
    prime_possible = 3
    end_num = 0
    while prime_list[end_num] != num:
        if is_prime(prime_possible):
            prime_list.append(prime_possible)
            prime_possible += 1
        else:
            prime_possible += 1


def goldbach(num):
    if num % 2 == 0:
        return None

    if is_prime(num - 2):
        new_list = [num - 2, 2]
        return new_list

    elif is_prime(num - 5):
        new_list = [num - 5, 5]
        return new_list



def face_smile():
    win = GraphWin('face', 400, 400)
    face_1 = Face(win, Point(200, 200), 100)
    face_1.wink(win)
    win.getMouse()
    win.close()


