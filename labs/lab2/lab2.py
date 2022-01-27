""""
Ethan Kidwell
lab2.py
Problem: Finding the different means based on different user inputs
I certify that this assignment is entirely my own work.
"""

import math


def means():
    loop_amount = eval(input("Please enter the amount of values to be entered: "))
    # gets the amount of values the users needs
    riemann_sum = 0
    harm_mean_sum = 0
    geo_mean_sum = 1
    # the accumulated sums
    for values in range(loop_amount):
        user_values = eval(input("Enter your value: "))
        riemann_sum = riemann_sum + user_values ** 2
        # takes the value entered and adds it as it's accumulator variable,setting the accumulator to the value squared,
        # then takes the second value and squares it and then adds that result to the accumulator and for the
        # loop amount
        harm_mean_sum = harm_mean_sum + (1 / user_values)
        # this takes the value and divides it by 1 and adds it to the accumulator variable, then proceeds to divide the
        # next input by 1 and adds it to the last product in the accumulator variable
        geo_mean_sum = geo_mean_sum * user_values
        # this takes the values and multiplies it by the next value in the sequence and then adds the result to the
        # accumulator variable

    r_m_s = math.sqrt(riemann_sum / loop_amount)
    # takes the accumulated values and divides them by the number of values in total
    h_m = loop_amount / harm_mean_sum
    # takes the accumulated sum of the values divided by one and then takes the number of values and divides it by the
    # accumulated sum
    g_m = math.pow(geo_mean_sum, 1 / loop_amount)
    # takes the accumulated product and takes it to the power of one over the numbers of values

    print("The value of root mean square: ", r_m_s)
    print("The value of harmonic mean: ", h_m)
    print("The value of geometric mean: ", g_m)
    # prints the totals


means()
