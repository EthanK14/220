"""
Name: Ethan Kidwell

Problem: Create a program that will find and remove a presented value from a list,
determines if the user input is between 1-10, tells the user how many digits are in
their number, make a game that picks a random number between 1-100 and allows
the user 7 guess and tells them if their guess is too high or low.

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""

from algorithms import read_data
from random import randint

def find_and_remove(num_list, value):
    index_val = num_list.index(value)  # finds
    num_list.pop(index_val)


def good_input():
    user_input = eval(input("Enter a number between 1-10: "))
    while not (user_input >= 1 and user_input <= 10):
        if user_input >= 1 and user_input <= 10:
            return user_input
        elif user_input < 1:
            print('Value too low')
        elif user_input > 10:
            print('Value too high')
        user_input = eval(input("Enter a number between 1-10: "))


def num_digits():
    user_input = eval(input('Enter a number (Enter a negative number or 0 to quit): '))
    while not (user_input <= 0):
        acc = 1
        while user_input // 10 != 0:
            user_input = user_input // 10
            acc += 1
        print('The numbers of digits are {}'.format(acc))
        user_input = eval(input('Enter a number (Enter a negative number or 0 to quit): '))


def hi_lo_game():
    random_num = randint(1, 100)
    print(random_num)
    user_guesses_num = 1
    print('You have 7 guesses to guess the number! :D')
    user_guess = eval(input("Guess a number between 1-100: "))

    if user_guess == random_num:
        print("You guessed the number!!!")
        print('It took 1 guess!')
        user_guesses_num = 8

    while user_guesses_num < 7 and not user_guess == random_num:

        if user_guess < random_num:
            print('Guess is too low')
            user_guesses_num = user_guesses_num + 1
            print('{} guesses left'.format(8 - user_guesses_num))

        elif user_guess > random_num:
            print('Guess is too high')
            user_guesses_num = user_guesses_num + 1
            print('{} guesses left'.format(8 - user_guesses_num))

        user_guess = eval(input("Guess a number between 1-100: "))

    if user_guess != random_num:
        print('You ran out of guess :(')
        print('The number was', random_num)
    elif user_guess == random_num:
        print("You guessed the number!!!")
        print('It took {} guesses!'.format(user_guesses_num - 1))


if __name__ == '__main__':
    # num_list = read_data('data_sorted.txt')
    # print(num_list)
    # find_and_remove(num_list, 75)
    # print(num_list)
    # good_input()
    # num_digits()
    hi_lo_game()