"""
Name: Ethan Kidwell
hw6.py

Problem: Make a function that converts a cash amount to a dollar amount,
encodes a message taken from the user, calculates the area and volume
of a sphere by taking the radius as an argument, and make a better
encoder based on a key.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import pi


def cash_converter():
    cash = eval(input("Enter a integer:"))
    cash = float(cash)
    dollar = "${:.2f}".format(cash)
    print(dollar)


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    new_message = ""
    for character in message:
        char = ord(character)
        new_val = key + char
        new_char = chr(new_val)
        new_message = new_message + new_char
    print(new_message)


def sphere_area(radius):
    s_area = ((radius ** 2) * pi) * 4
    return s_area


def sphere_volume(radius):
    volume = ((radius ** 3) * pi) * (4 / 3)
    return volume


def sum_n(number):
    num = 0
    for i in range(number + 1):
        num = num + i
    return num


def sum_n_cubes(number):
    num = 0
    for i in range(number + 1):
        num = num + (i ** 3)
    return num


def encode_better():
    message = input("Enter a message: ")
    keyword = input("Enter a keyword: ")
    new_message = ""
    key_len = len(keyword)  # gets length of keyword to loop through it
    acc = 0
    # message = message.upper()
    # keyword = keyword.upper()
    # message = message.replace(" ", "")
    # keyword = keyword.replace(" ", "")

    for character in message:
        accu = acc % key_len  # doesn't allow it to ge out of range of slice
        mess_val = ord(character)
        key_char = keyword[accu]  # pulls the character of the keyword
        key_val = ord(key_char)
        mess_dif = mess_val - 65
        difference = key_val - 65
        mod_dif = (mess_dif + difference) % 58
        new_int = mod_dif + 65
        new_char = chr(new_int)
        new_message = new_message + new_char
        acc = acc + 1  # accumulator part
    print(new_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
