"""
Name: Ethan Kidwell
hw2.py

Problem: To make different functions' computer different equations. These being sum of numbers by
threes, making a multiplication table, computing area of a triangle, sum of square roots,
and creating a function to raise some number to a power

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    # gets the upper bound from the user
    true_upper = upper_bound + 1
    # allows the loop to add the final value to the sum
    three_sum = 0
    # accumulator variable
    for add_threes in range(3, true_upper, 3):
        three_sum = three_sum + add_threes
    print("Sum of threes is ", three_sum)


def multiplication_table():
    for top in range(1, 11):
        print("\n")
        for side in range(1, 11):
            print(top * side, end=" ")


def triangle_area():
    side_a = eval(input("Enter side A: "))
    side_b = eval(input("Enter side B: "))
    side_c = eval(input("Enter side C: "))
    step_one = (side_a + side_b + side_c) / 2
    step_two = math.sqrt(step_one * ((step_one - side_a) * (step_one - side_b) * (step_one - side_c)))
    print("The area is: ", step_two)


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    true_upper = upper_range + 1
    acc = 0
    for square in range(lower_range, true_upper):
        acc = acc + (square * square)
    print(acc)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    # true_exponent = exponent + 1
    acc = 1
    for power_man in range(exponent):
        acc = acc * base
        print(acc)
    print(base, "^", exponent, "=", acc)


if __name__ == '__main__':
    pass
