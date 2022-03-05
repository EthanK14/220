"""
Name: Ethan Kidwell
hw7.py

Problem: Create a program that numbers the words in a file and list them, tha raises each employee's pay by 1.65
and calculate that weeks pay, a calculator that gets the check sum of a ISBN,
that changes the name of the file to that of the recipient, sends a secret message to a friend,
creates a file with an uncrackable message to a friend.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from encryption import encode_better


def number_words(in_file_name, out_file_name):
    input_file = open(in_file_name, 'r')
    output_file = open(out_file_name, 'w')
    word_seq = input_file.read()
    word_seq = word_seq.lstrip()
    word_seq = word_seq.rstrip()
    word_seq = word_seq.replace("\n", " ")
    word_list = word_seq.split(" ")
    seq_num = 1
    for word in word_list:
        num_word = "{} {}".format(seq_num, word)
        seq_num = seq_num + 1
        print(num_word, file=output_file)


def hourly_wages(in_file_name, out_file_name):
    input_file = open(in_file_name, 'r')
    output_file = open(out_file_name, 'w')
    for raise_wage in input_file:
        pay_list = raise_wage.split(" ")
        pay_rate = (pay_list[2])
        pay_rate = float(pay_rate)
        hour_work = (pay_list[3])
        hour_work = float(hour_work)
        new_rate = pay_rate + 1.65
        bonus_pay = new_rate * hour_work
        new_pay = "{} {} {:.2f}".format(pay_list[0], pay_list[1], bonus_pay)
        print(new_pay, file=output_file)


def calc_check_sum(isbn):
    check_sum = isbn
    check_val = check_sum.replace("-", "")
    # check_val = len(check_sum)
    check_index = 10
    check_total = 0
    for check in check_val:
        check = int(check)
        check_prt = check * check_index
        check_total = check_total + check_prt
        check_index = check_index - 1
    return check_total


def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    file_name = "{}.txt".format(friend_name)
    out_file = open(file_name, 'w')
    read = in_file.read()
    print(read[0:-1], file=out_file)


def encode(message_from, key):
    message = message_from
    key = int(key)
    new_message = ""
    for character in message:
        char = ord(character)
        new_val = key + char
        new_char = chr(new_val)
        new_message = new_message + new_char
    return new_message


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    file_name = "{}.txt".format(friend_name)
    out_file = open(file_name, 'w')
    read = in_file.read()
    new_message = encode(read[:-1], key)
    print(new_message, file=out_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, 'r')
    key = open(pad_file_name, 'r')
    key_format = key
    file_name = "{}.txt".format(friend_name)
    out_file = open(file_name, 'w')
    read = in_file.read()
    new_message = encode_better(read, key_format)
    print(new_message, file=out_file)


if __name__ == '__main__':
    pass
