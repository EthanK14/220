"""
Name: Ethan Kidwell
hw3.py

Problem: We must use loops to find average of grades, total amount of tips, compute square roots,
print a sequence, and calculate pi using a specified amount of terms.

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""


def average():
    grade_amount = eval(input("How many grades will you enter? "))
    grade_total = 0
    for grade in range(grade_amount):
        grade_entered = eval(input("Enter your grade: "))
        grade_total = grade_total + grade_entered
    grade_average = grade_total / grade_amount
    print('Your average is: ', grade_average)


def tip_jar():
    total_tips = 0
    for tips in range(5):
        tip_amount = eval(input("How much you would like to donate? "))
        total_tips = total_tips + tip_amount
    print("Total tips: $", total_tips)


def newton():
    square_root = eval(input("Please enter your square root: "))
    approximate = square_root
    square_approx = eval(input("How many times should we improve the approximation? "))
    for root in range(square_approx):
        approximate = .5 * (approximate + square_root / approximate)
    print(approximate)


def sequence():
    seq_num = eval(input("How many terms would you like? "))
    for seq in range(1, seq_num + 1):
        odd_nums = (seq - 1) + (seq % 2)
        print(odd_nums, end=" ")


def pi():
    term_num = eval(input("How many terms in the series? "))
    acc = 1
    for pi_loop in range(term_num):
        numerator_seq = pi_loop + (2 - (pi_loop % 2))
        denominator_seq = pi_loop + (1 + (pi_loop % 2))
        acc = acc * (numerator_seq / denominator_seq)
    pi_approx = acc * 2
    print(pi_approx)



if __name__ == '__main__':
    pass
