from random import randint
from graphics import *


def get_words(file_name):
    txt_file = open(file_name, 'r')  # opens the file for reading
    word_list = []  # creates new word list for the words from the file
    acc = 0  # accumulator for looping through file
    for word in txt_file:  # loop to go through the file and adds it to a list
        word_list = word_list[acc] + word  # adds the word to the list
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
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    # accumulator to loop through the index for the secret word

    new_word = secret_word
    # loops through the secret word to check it against the guessed list

    for letter in new_word:
        # checks the letter against all the letters in the guessed list
        acc = 0
        for guessed in guesses:

            # actually does the checking of the list
            if not (ord(guessed) - ord(letter)):
                new_word = new_word.replace(new_word[acc], letter)

            # adds the _ if no guess was that letter
            elif ord(guessed) - ord(letter):
                new_word = new_word.replace(new_word[acc], '_')
        # makes sure the correct letter is replaced either by the correctly guessed letter or the _
            acc = acc + 1
    return new_word


def won(guessed):
    for character in guessed:
        if character == '_':
            return False
    return True


def play_graphics(secret_word):
    # create the window
    length = 500
    height = 800
    win = GraphWin("Hangman", length, height)

    # creates the gallows
    bottom = Line(Point(150, height - 200), Point(350, 600))

    # draws the objects


def play_command_line(secret_word):
    num_of_guess = 6
    guesses_list = []
    len_secret_word = len(secret_word)
    for solve in range(len_secret_word):
        print("Already guessed: {}".format(guesses_list))
        print("Number of guesses left: {}".format(num_of_guess))
        hidden_word = make_hidden_secret(secret_word, guesses_list)
        print(hidden_word)
        letter_input = input("Enter a letter to guess: ")
        if already_guessed(letter_input, guesses_list):
            pass
        elif letter_in_secret_word(letter_input, secret_word):
            guesses_list.append(letter_input)
            # hidden_word = make_hidden_secret
        elif won(hidden_word):
            print("Player Won!!! :D The Secret Word was {}".format(secret_word))
        elif num_of_guess == 0:
            print("Sorry you ran out of guesses. :'( The secret word was {}".format(secret_word))
        elif not letter_in_secret_word(letter_input, secret_word):
            num_of_guess = num_of_guess - 1



if __name__ == '__main__':
    pass
    # play_command_line("secret word")
    # play_graphics(secret_word)
