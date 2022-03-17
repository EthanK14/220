"""
Name: Ethan Kidwell
lab8.py

Problem: Write a program that simulates two bumper cars that when they collide they
nuance off in different directions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time
from random import randint
from math import sqrt
from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle_ball, circle_ball_2):
    circle_1_rad = circle_ball.getRadius()
    circle_2_rad = circle_ball_2.getRadius()
    circles_rad = circle_1_rad + circle_2_rad
    circle_1_center = circle_ball.getCenter()
    circle_2_center = circle_ball_2.getCenter()
    circle_1_x, circle_1_y = circle_1_center.getX(), circle_1_center.getY()
    circle_2_x, circle_2_y = circle_2_center.getX(), circle_2_center.getY()
    circle_distance = sqrt(((circle_2_x - circle_1_x) ** 2)+((circle_2_y - circle_1_y) ** 2))
    if circle_distance >= circles_rad:
        return True
    else:
        return False


def hit_vertical(circle_ball, graphwin):
    circle_rad = circle_ball.getRadius()
    win_height = graphwin.getHeight()
    rad_dif = circle_rad - win_height  # finds the length between radius and top or bottom
    rad_dis = win_height - rad_dif  # finds the length of the radius
    # circle_1_center = circle_ball.getCenter()
    # circle_1_x, circle_1_y = circle_1_center.getX(), circle_1_center.getY()
    if circle_rad <= rad_dis:
        return True
    else:
        return False


def hit_horizontal(circle_ball, graphwin):
    circle_rad = circle_ball.getRadius()
    win_width = graphwin.getWidth()
    rad_dif = circle_rad - win_width  # finds the length between radius and top or bottom
    rad_dis = win_width - rad_dif  # finds the length of the radius
    if circle_rad <= rad_dis:
        return True
    else:
        return False


def get_random_color():
    rgb1 = randint(0, 255)
    rgb2 = randint(0, 255)
    rgb3 = randint(0, 255)
    ran_color = color_rgb(rgb1, rgb2, rgb3)
    return ran_color


def bumper():
    # creates the window object as well as the circle objects at random points
    win = GraphWin("Bumper Cars", 800, 600)
    win_height = win.getHeight()
    win_width = win.getWidth()

    # random circle radius
    ran_rad_1 = randint(10, 100)
    # random circle location
    ran_x_1 = randint(ran_rad_1, win_width)
    ran_y_1 = randint(ran_rad_1, win_height)
    ran_x_2 = randint(ran_rad_1, win_width)
    ran_y_2 = randint(ran_rad_1, win_height)

    # create the circles at their random points on the window
    circle_1 = Circle(Point(ran_x_1, ran_y_1), ran_rad_1)
    circle_2 = Circle(Point(ran_x_2, ran_y_2), ran_rad_1)

    # colors the circles with random color
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())

    # Draws the objects to the window in their random location
    circle_1.draw(win)
    circle_2.draw(win)

    # moves the circles
    while True:
        ran_move = get_random(10)
        circle_1.move(10, 10)
        circle_2.move(10, 10)
        time.sleep(.5)
        if hit_vertical(circle_1, win):
                circle_1.move(-ran_move, ran_move)
                circle_1.move(ran_move, -ran_move)


        # if did_collide(circle_1, circle_2):




    # click_close = Text(Point(win.getWidth() / 2, win.getHeight() / ), "Click anywhere to close")
    # click_close.draw(win)
    win.getMouse()
    win.close()


bumper()
