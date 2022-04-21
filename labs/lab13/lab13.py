"""
Name: Ethan Kidwell

Problem: Create a program that will take the signal strength
from a file and use it to determine if it is a neutron star by
seeing if it has strength between 4000 - 5000 five times
in a row.

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""


def star_find(file_name):
    star_data = open(file_name, 'r')  # opens the file to read
    star_list = star_data.readline().split(' ')  # takes the line in the file and converts it into a list
    # looks for recurring signal between 4000-5000
    # loops through data
    acc = 0
    star_found = []
    # while not acc == 5:
    for nums in star_list:
        if 5000 >= int(nums) >= 4000:
            star_found.append(int(nums))
            acc = acc + 1

    if acc >= 5:
        nums_changed = star_list.index(str(star_found[4]))
        print('Number of signals found: 5')
        print('Signal values found: {}'.format(star_found[:5]))
        print('Number of signals searched until five where found: {}'.format(nums_changed))
        print(len(star_list))
        # print(star_list.index('4345'))
    elif acc :
        print('Number of signals found: {}'.format(acc))
        print('Signal values found: {}'.format(star_found))






if __name__ == '__main__':
    star_find('test.txt')
