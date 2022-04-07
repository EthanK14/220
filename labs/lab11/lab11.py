"""
Name: Ethan Kidwell
Problem: Create a game that uses both button and door classes to create a game where
you have to guess the correct door from three doors and keeps tracks of
your wins and loses.

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""

from lab10.button import Button
from lab10.door import Door
from graphics import GraphWin, Point, Rectangle, Text
from random import randint


def three_door_game():
    # creating all the objects for the game
    # the window
    length = 800
    height = 600
    win = GraphWin("Three Door Game", length, height)
    win.setBackground('light blue')

    # creates the doors rectangles
    door_1_rectangle = Rectangle(Point(150, 250), Point(250, 450))
    door_2_rectangle = Rectangle(Point(350, 250), Point(450, 450))
    door_3_rectangle = Rectangle(Point(550, 250), Point(650, 450))

    # creates the button rectangle
    exit_rectangle = Rectangle(Point(550, 50), Point(650, 100))

    # creates the door objects
    door_1 = Door(door_1_rectangle, 'Door 1')
    door_1.color_door('grey')
    door_2 = Door(door_2_rectangle, 'Door 2')
    door_2.color_door('grey')
    door_3 = Door(door_3_rectangle, 'Door 3')
    door_3.color_door('grey')

    # creates the button objects

    exit_button = Button(exit_rectangle, 'Quit')

    # score board
    wining_score = '0'
    losing_score = '0'
    winner_text = Text(Point(175, 40), 'Wins')
    losses_text = Text(Point(225, 40), 'Losses')
    score_board_winner = Rectangle(Point(150, 50), Point(200, 100))
    score_board_loser = Rectangle(Point(200, 50), Point(250, 100))
    winner_score = Text(score_board_winner.getCenter(), wining_score)
    loser_score = Text(score_board_loser.getCenter(), losing_score)

    # creates the direction text

    pick_instruct = Text(Point(400, 150), 'Pick the Secret Door! :D')
    clicking_instruct = Text(Point(400, 500), 'Click a door to guess! ~_~')

    # draws everything to a window
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    exit_button.draw(win)
    score_board_loser.draw(win)
    score_board_winner.draw(win)
    winner_score.draw(win)
    loser_score.draw(win)
    winner_text.draw(win)
    losses_text.draw(win)
    clicking_instruct.draw(win)
    pick_instruct.draw(win)
    user_click = win.getMouse()

    # loop for the game
    while not exit_button.is_clicked(user_click):

        # draws the doors and resets everything for a new game
        door_1.color_door('grey')
        door_1.set_label('Door 1')
        door_2.color_door('grey')
        door_2.set_label('Door 2')
        door_3.color_door('grey')
        door_3.set_label('Door 3')

        # resets text for new game
        pick_instruct.setText('Pick the Secret door! :D')
        clicking_instruct.setText('Click a door to guess! ~_~')

        # makes random door a secret door
        secret_picker = randint(1, 3)
        if secret_picker == 1:
            door_1.set_secret(0)
            door_2.set_secret(1)
            door_3.set_secret(1)
        elif secret_picker == 2:
            door_1.set_secret(1)
            door_2.set_secret(0)
            door_3.set_secret(1)
        elif secret_picker == 3:
            door_1.set_secret(1)
            door_2.set_secret(1)
            door_3.set_secret(0)

        if door_1.is_clicked(user_click):
            if door_1.is_secret():
                # changes the door to green if correct
                door_1.color_door('green')

                # changes the text to you won if the correct door picked
                pick_instruct.undraw()
                pick_instruct.setText('You Won!!!')
                pick_instruct.draw(win)

                # changes the score up one on the winning side
                wining_score = int(winner_score.getText())
                wining_score = wining_score + 1
                winner_score.setText(wining_score)

                # changes the instruction text to tell the user to click anywhere to play again
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)

            if not door_1.is_secret():
                # changes the door to red if incorrect
                door_1.color_door('dark red')

                # changes the text to tell the user they choose the incorrect door
                pick_instruct.undraw()
                pick_instruct.setText('Sorry, incorrect :(')
                pick_instruct.draw(win)

                # adds one to the losses on the score board
                losing_score = int(loser_score.getText())
                losing_score = losing_score + 1
                loser_score.setText(losing_score)

                # changes the instruction to tell the user to press again to play
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)

        elif door_2.is_clicked(user_click):
            if door_2.is_secret():
                # changes the door to green if correct
                door_2.color_door('green')

                # changes the text to you won if the correct door picked
                pick_instruct.undraw()
                pick_instruct.setText('You Won!!!')
                pick_instruct.draw(win)

                # changes the score up one on the winning side
                wining_score = int(winner_score.getText())
                wining_score = wining_score + 1
                winner_score.setText(wining_score)

                # changes the instruction text to tell the user to click anywhere to play again
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)

            if not door_2.is_secret():
                # changes the door to red if incorrect
                door_2.color_door('dark red')

                # changes the text to tell the user they choose the incorrect door
                pick_instruct.undraw()
                pick_instruct.setText('Sorry, incorrect :(')
                pick_instruct.draw(win)

                # adds one to the losses on the score board
                losing_score = int(loser_score.getText())
                losing_score = losing_score + 1
                loser_score.setText(losing_score)

                # changes the instruction to tell the user to press again to play
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)
        elif door_3.is_clicked(user_click):
            if door_3.is_secret():
                # changes the door to green if correct
                door_3.color_door('green')

                # changes the text to you won if the correct door picked
                pick_instruct.undraw()
                pick_instruct.setText('You Won!!!')
                pick_instruct.draw(win)

                # changes the score up one on the winning side
                wining_score = int(winner_score.getText())
                wining_score = wining_score + 1
                winner_score.setText(wining_score)

                # changes the instruction text to tell the user to click anywhere to play again
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)

            if not door_3.is_secret():
                # changes the door to red if incorrect
                door_3.color_door('dark red')

                # changes the text to tell the user they choose the incorrect door
                pick_instruct.undraw()
                pick_instruct.setText('Sorry, incorrect :(')
                pick_instruct.draw(win)

                # adds one to the losses on the score board
                losing_score = int(loser_score.getText())
                losing_score = losing_score + 1
                loser_score.setText(losing_score)

                # changes the instruction to tell the user to press again to play
                clicking_instruct.undraw()
                clicking_instruct.setText('Click anywhere to play again')
                clicking_instruct.draw(win)
        user_click = win.getMouse()

    win.close()


if __name__ == '__main__':
    three_door_game()
