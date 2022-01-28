"""
Name: Ethan Kidwell
hw1.py

Problem: In this assignment you must make simple problem-solving programs. Including to calculate
the area and volume of a rectangle, shooting percentage, coffee per pound, and kilometers to miles.
Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the Length: "))
    #Gets the length from the user
    width = eval(input("Enter the width: "))
    #Gets the width from the user
    area = length * width
    #Does the equation to find area
    print("Area =", area)
    #prints the area

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * height * width
    print("Volume =", volume)




def shooting_percentage():
    total_shots = eval(input("Enter the payers total shots: "))
    made_shots = eval(input("Enter how many shots the player made: "))
    shoot_percent = (made_shots / total_shots) * 100
    print("Shooting percentage: ", shoot_percent, "%")


def coffee():
    coffee_pounds = eval(input("How many pounds of coffee would you like? "))
    price = (coffee_pounds * 11.36) + 1.50
    print("Your total is $", price)


def kilometers_to_miles():
    kilometer = eval(input("How many kilometers did you travel? "))
    mile = kilometer / 1.61
    print("You traveled", mile, "miles!")
if __name__ == '__main__':
    pass
