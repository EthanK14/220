"""
Ethan Kidwell
lab6.py

Problem: Create a vigenere cypher that takes a message from the user and encodes it
based on a key word provided from the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def vigenere():
    # creates the window
    length = 500
    width = 300
    win = GraphWin("Vigenere", length, width)

    # creates the entry boxes and text
    entry_x = 225
    entry_y = 50
    message_text = Text(Point(entry_x - 100, entry_y), "Enter Message:")
    keyword_text = Text(Point(entry_x - 100, entry_y + 25), "Enter Keyword:")
    message_box = Entry(Point(entry_x + 77, entry_y), 25)
    keyword_box = Entry(Point(entry_x + 10, entry_y + 25), 10)
    encode_button = Rectangle(Point(entry_x - 3, 150 - 12.5), Point(entry_x + 53, 150 + 12.5))
    encode_text = Text(Point(250, 150), "Encode")
    result_mess = Text(Point(250, 200), "Resulting Message:")
    result_text = Text(Point(250, 225), " ")
    close_text = Text(Point(250, 280), " ")
    temp_res = Text(Point(250, 250), " ")

    # draws all objects to the window
    message_text.draw(win)
    message_box.draw(win)
    keyword_text.draw(win)
    keyword_box.draw(win)
    encode_text.draw(win)
    encode_button.draw(win)
    result_mess.draw(win)
    result_text.draw(win)
    close_text.draw(win)
    temp_res.draw(win)

    # gets text box text
    win.getMouse()
    message = message_box.getText()
    keyword = keyword_box.getText()

    # edits message and key to be computed
    message = message.upper()
    keyword = keyword.upper()
    message = message.replace(" ", "")

    # computes the cypher
    new_message = ""
    key_len = len(keyword)  # gets length of keyword to loop through it
    acc = 0

    for character in message:
        # gets the values of individual characters
        accu = acc % key_len  # doesn't allow it to ge out of range of slice
        mess_val = ord(character)
        key_char = keyword[accu]  # pulls the character of the keyword
        key_val = ord(key_char)

        # changes the character values from 0 -> 25
        mess_dif = mess_val - 65
        difference = key_val - 65

        # begins the calculations for the cypher
        mod_dif = (mess_dif + difference) % 26
        new_int = mod_dif + 65
        new_char = chr(new_int)
        new_message = new_message + new_char
        acc = acc + 1  # accumulator part

    # sets result text
    result_text.setText(new_message)
    # temp_res.setText(keyword)

    # click to close message
    close_text.setText("Click to Close")
    win.getMouse()
    win.close()


vigenere()
