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
    pass


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
