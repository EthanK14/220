"""
Name: Ethan Kidwell
Problem: Create a program that uses button.py and door.py to create a
opening and closing door.

Certificate of Authenticity:
Certification of Authenticity:
I certify that this assignment is entirely my own work, and I disused it with: Brooks (CSL)
"""

from graphics import Text


class Button:
    def __init__(self, shape, label):
        self.rectangle = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text = self.text.setText(label)

    def draw(self, win):
        self.rectangle.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.rectangle.undraw()
        self.text.undraw()

    def is_clicked(self, point_clicked):
        p_1 = self.rectangle.getP1()
        p_2 = self.rectangle.getP2()
        x_1 = p_1.getX()
        y_1 = p_1.getY()
        x_2 = p_2.getX()
        y_2 = p_2.getY()
        point_x = point_clicked.getX()
        point_y = point_clicked.getY()
        if (x_1 <= point_x and x_2 >= point_x) and (y_1 <= point_y and y_2 >= point_y):
            return True
        return False

    def color_button(self, color):
        self.rectangle.setFill(color)
