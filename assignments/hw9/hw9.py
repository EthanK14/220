from random import randint


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


def already_guessed(letter, guesses,):
    for guess in guesses:
        if guess == letter:
            return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    pass


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
