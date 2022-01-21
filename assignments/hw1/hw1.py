"""
Name: Ethan Kidwell
hw1.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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
    pass


def kilometers_to_miles():
    pass


if __name__ == '__main__':
    pass
