from graphics import Text


class Door:
    def __init__(self, shape, label):
        self.rectangle = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = 0  # 0 mean secret door is false 1 and above mean it Is secret door
        self.door_state = 0  # 0 mean close and 1 mean open

    def get_label(self):
        return self.text.getText()

    def get_state(self):
        return self.door_state

    def set_label(self, label):
        self.text.setText(label)

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

    def open(self, color, label):
        self.rectangle.setFill(color)
        self.text.setText(label)
        self.door_state = 1

    def close(self, color, label):
        self.rectangle.setFill(color)
        self.text.setText(label)
        self.door_state = 0

    def color_door(self, color):
        self.rectangle.setFill(color)

    def is_secret(self):
        if not self.secret:  # if 0 (false) then return it as not secret
            return False
        return True

    def set_secret(self, secret_value):
        self.secret = secret_value
