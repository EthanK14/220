from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def __get_size(self):
        return self.head.getRadius()

    def __get_window(self):
        return self.window

    def smile(self, window):
        point_left = self.mouth.getP1()
        point_right = self.mouth.getP2()
        point_3 = self.head.getCenter()
        point_3_x = point_3.getX()
        point_3_y = point_3.getY()
        point_3_real = Point(point_3_x, (self.__get_size() / 2) + point_3_y + 15)
        mouth_left = Line(point_3_real, point_left)
        mouth_right = Line(point_3_real, point_right)
        mouth_right.draw(window)
        mouth_left.draw(window)

    def shock(self, window):
        # new_mouth = self.left_eye.clone()
        self.mouth.undraw()
        point_3 = self.head.getCenter()
        point_3_x = point_3.getX()
        point_3_y = point_3.getY()
        new_mouth = Circle(Point(point_3_x, (self.__get_size() / 2) + point_3_y + 15), 0.15 * self.__get_size())
        new_mouth.draw(window)

    def wink(self, window):
        point_left = self.mouth.getP1()
        point_right = self.mouth.getP2()
        point_3 = self.head.getCenter()
        point_3_x = point_3.getX()
        point_3_y = point_3.getY()
        point_3_real = Point(point_3_x, (self.__get_size() / 2) + point_3_y + 15)
        mouth_left = Line(point_3_real, point_left)
        mouth_right = Line(point_3_real, point_right)
        self.left_eye.undraw()
        self.left_eye.getCenter()
        point_1 = Point(self.left_eye.getCenter().getX() - 10, self.left_eye.getCenter().getY())
        point_2 = Point(self.left_eye.getCenter().getX() + 10, self.left_eye.getCenter().getY())
        winky = Line(point_1, point_2)
        winky.draw(window)
        mouth_right.draw(window)
        mouth_left.draw(window)
