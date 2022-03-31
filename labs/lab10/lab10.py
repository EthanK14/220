from button import Button
from door import Door
from graphics import Rectangle, Point, Text, GraphWin


def main():
    length = 800
    height = 600
    win = GraphWin("Door", length, height)

    exit_rectangle = Rectangle(Point(300, 100), Point(600, 100))
    exit_button = Button(exit_rectangle, "Exit")
    exit_button.draw(win)

    door_rectangle = Rectangle(Point(300, 300), Point(600, 500))
    door_made = Door(door_rectangle, "Open")
    user_click = win.getMouse()
    door_made.draw(win)
    if exit_button.is_clicked(user_click):
        win.close()
    if door_made.is_clicked(user_click):
        door_made.open('white', 'OPEN')
        door_made.draw(win)


if __name__ == '__main__':
    main()