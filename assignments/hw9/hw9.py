"""
Name: Ethan Kidwell
Problem: Create a program that plays hangman in both the console and
in a graphics window.

Certificate of Authenticity:
Certification of Authenticity:
I certify that this assignment is entirely my own work, and I disused it with: Brooks (CSL)
"""
from random import randint
from graphics import *


def get_words(file_name):
    txt_file = open(file_name, 'r')  # opens the file for reading
    word_list = []  # creates new word list for the words from the file
    acc = 0  # accumulator for looping through file
    for word in txt_file:  # loop to go through the file and adds it to a list
        word_list.append(word)  # adds the word to the list
        acc = acc + 1
    return word_list  # returns the list


# word_list = ["word\n", "find\n"]

def get_random_word(words):
    word_list_len = len(words)  # gets the length of the list to find an element to return
    ran_num = randint(0, word_list_len - 1)  # gets a random number that is range of the list
    secret_word = words[ran_num]
    return secret_word[:-1]


def letter_in_secret_word(letter, secret_word):
    find_letter = secret_word.find(letter)
    if find_letter >= 0:
        return True
    return False


def already_guessed(letter, guesses):
    for guess in guesses:
        if guess == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    # accumulator to loop through the index for the secret word

    new_word = []
    secret_word_len = len(secret_word)
    for _ in range(secret_word_len):
        new_word.append('_ ')

    # loops through the secret word to check it against the guessed list

    for letter in range(secret_word_len):
        # checks the letter against all the letters in the guessed list
        for guessed in guesses:

            # adds the _ if no guess was that letter
            if ord(guessed) - ord(secret_word[letter]) == 0:
                new_word[letter] = guessed + ' '
        # makes sure the correct letter is replaced either by the correctly guessed letter or the _
    return ''.join(new_word).rstrip()


def won(guessed):
    for character in guessed:
        if character == '_':
            return False
    return True


def play_graphics(secret_word):
    # create the window
    length = 800
    height = 700
    win = GraphWin("Hangman", length, height)

    # creates the gallows
    bottom = Line(Point(300, 500), Point(500, 500))
    stem = Line(Point(450, 50), Point(450, 500))
    top_part = Line(Point(450, 50), Point(300, 50))
    rope = Line(Point(300, 100), Point(300, 50))
    head = Circle(Point(300, 150), 50)
    body = Line(Point(300, 300), Point(300, 350))
    arm_1 = Line(Point(300, 220), Point(330, 290))
    arm_2 = Line(Point(300, 220), Point(270, 290))
    leg_1 = Line(Point(300, 450), Point(330, 420))
    leg_2 = Line(Point(300, 350), Point(270, 420))

    # create the text objects to be printed
    game_condition = Text(Point(400, 525), '')
    already_guessed_text = Text(Point(400, 625), '')
    user_guess_entry = Entry(Point(425, 650), 2)
    user_guess_text = Text(Point(355, 650), "Guess a Letter:")
    hidden_word_text = Text(Point(400, 600), '')

    # draws the gallows and text needed
    bottom.draw(win)
    stem.draw(win)
    top_part.draw(win)
    rope.draw(win)
    user_guess_entry.draw(win)
    user_guess_text.draw(win)

    # the game
    num_of_guess = 6
    guesses_list = []
    already_guessed_text.setText("Already guessed: {}".format(guesses_list))
    hidden_word = make_hidden_secret(secret_word, guesses_list)
    hidden_word_text.setText(hidden_word)
    already_guessed_text.draw(win)
    hidden_word_text.draw(win)


    while won(guesses_list):
        user_guess_entry.undraw()
        user_guess_entry.draw(win)

        # entry box and other text
        hidden_word = make_hidden_secret(secret_word, guesses_list)
        if won(hidden_word):
            game_condition.undraw()
            game_condition.setText("Player Won!!! :D The Secret Word was {}".format(secret_word))
            game_condition.draw(win)
            hidden_word_text.undraw()
            hidden_word_text.setText(hidden_word)
            hidden_word_text.draw(win)
            break
        if num_of_guess == 0:
            game_condition.undraw()
            game_condition.setText("Sorry you ran out of guesses. :'(")
            game_condition.draw(win)
            hidden_word_text.undraw()
            hidden_word_text.setText(hidden_word)
            hidden_word_text.draw(win)
            break
        already_guessed_text.undraw()
        already_guessed_text.setText("Already guessed: {}".format(guesses_list))
        already_guessed_text.draw(win)
        hidden_word_text.undraw()
        hidden_word_text.setText(hidden_word)
        hidden_word_text.draw(win)
        win.getMouse()
        if already_guessed(user_guess_entry.getText(), guesses_list):
            pass
        elif letter_in_secret_word(user_guess_entry.getText(), secret_word):
            guesses_list.append(user_guess_entry.getText())

        elif not letter_in_secret_word(user_guess_entry.getText(), secret_word):
            num_of_guess = num_of_guess - 1
            guesses_list.append(user_guess_entry.getText())
            if num_of_guess == 5:
                head.draw(win)
            elif num_of_guess == 4:
                body.draw(win)
            elif num_of_guess == 3:
                arm_1.draw(win)
            elif num_of_guess == 2:
                arm_2.draw(win)
            elif num_of_guess == 1:
                leg_1.draw(win)
            elif num_of_guess == 0:
                leg_2.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    num_of_guess = 6
    guesses_list = []
    while won(guesses_list):
        hidden_word = make_hidden_secret(secret_word, guesses_list)
        if won(hidden_word):
            print("Player Won!!! :D The Secret Word was {}".format(secret_word))
            print(hidden_word)
            break
        if num_of_guess == 0:
            print("Sorry you ran out of guesses. :'( The secret word was {}".format(secret_word))
            break
        print("Already guessed: {}".format(guesses_list))
        print("Number of guesses left: {}".format(num_of_guess))
        print(hidden_word)
        letter_input = input("Enter a letter to guess: ")
        if already_guessed(letter_input, guesses_list):
            pass
        elif letter_in_secret_word(letter_input, secret_word):
            guesses_list.append(letter_input)


        elif not letter_in_secret_word(letter_input, secret_word):
            num_of_guess = num_of_guess - 1
            guesses_list.append(letter_input)


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
