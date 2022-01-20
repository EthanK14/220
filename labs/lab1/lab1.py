"""
Ethan Kidwell
lab1.py
Problem: Create a program that can determine monthly interest rate based on information provided by a user.
I certify that this assignment is entirely my own work.
"""


def monthly_interest():
    annintrate = eval(input("Please enter your annual interest rate: "))
    # Gets the anual interest rate
    dayincyc = eval(input("Please enter the number of days in your billing cycle: "))
    # Gets the number of days in the billing cycle
    netbal = eval(input("Please enter your current balance: "))
    # Gets the net balance
    netpaymn = eval(input("Please enter your payment amount: "))
    # Gets the payment amount
    payday = eval(input("Please enter the day of payment: "))
    # Gets the day of the month the payment was made
    stepone = netbal * dayincyc
    # stepone is takeing the net balance and the number of days
    # in the billing cycle and multiplies them
    steptwo = netpaymn * (dayincyc - payday)
    stepthree = stepone - steptwo
    avgdaybal = stepthree / dayincyc
    # gets the average daily balance
    monthlyintratewhole = annintrate / 12
    # takes the annual rate and turns it into the monthly rate
    monthlyintrate = monthlyintratewhole / 100
    # turns the montly rate into a decimal
    mntinterest = monthlyintrate * avgdaybal
    print("Your monthly interest is $", mntinterest)

monthly_interest()