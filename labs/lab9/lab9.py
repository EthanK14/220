"""
Name: Ethan Kidwell
lab9.py

Problem: Build a tic-tac-toe game that instructs the user how to play and
then determines the winner and ask if you want to play again.

Certificate of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke in CSL 
"""


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    bord_check = str(board[position - 1]).isnumeric()
    return bord_check


def fill_spot(board, position, character):
    board[position - 1] = character


def winning_game(board):
    # accumulator variable
    position = 0

    # checks the horizontal range on the board
    for horizontal in range(3):

        # checks if x's or o's have 3 in a row
        if ord(str(board[position])) == ord(str(board[position + 1])) == ord(str(board[position + 2])):
            return True
        position = position + 3

    # restates accumulators for vertical checks
    position = 0

    # checks the vertical values
    for vertical in range(3):
        if ord(str(board[position])) == ord(str(board[position + 3])) == ord(str(board[position + 6])):
            return True
        position = position + 1

    # these all check the cross sections
    if ord(str(board[2])) == ord(str(board[4])) == ord(str(board[6])):
        return True
    if ord(str(board[0])) == ord(str(board[4])) == ord(str(board[8])):
        return True
    return False


test_list = [1,2,3,4,5,6,7,8,9]


def game_over(board):
    if winning_game(board):
        return True
    acc = 0
    if_number = 0
    for game in range(len(board)):
        if not str(board[game]).isnumeric():
            if_number = if_number + 1
        acc = acc + 1
    if if_number == 9:
        return True
    return False


def get_winner(board):
    # accumulator variables
    position = 0
    position_o = 0

    # checks the horizontal range on the board
    for horizontal in range(3):

        # checks if x's have 3 in a row
        if (ord(str(board[position])) + ord(str(board[position + 1])) + ord(str(board[position + 2]))) == 360:
            return 'x'
        position = position + 3

        # checks if o's have 3 in a row
        if (ord(str(board[position_o])) and ord(str(board[position_o + 1])) and ord(str(board[position_o + 2]))) == 333:
            return 'o'
        position_o = position_o + 3

        # restates accumulators for vertical checks
        position = 0
        position_o = 0

        # checks if x's have 3 in a column
        if (ord(str(board[position])) + ord(str(board[position + 3])) + ord(str(board[position + 6]))) == 360:
            return 'x'
        position = position + 1

        # checks if o's have 3 in a column
        if (ord(str(board[position_o])) and ord(str(board[position_o + 3])) and ord(str(board[position_o + 6]))) == 333:
            return 'o'
        position_o = position_o + 1

    # these all check the cross sections
    if (ord(str(board[2])) and ord(str(board[4])) and ord(str(board[6]))) == 360:
        return 'x'
    if (ord(str(board[2])) and ord(str(board[4])) and ord(str(board[6]))) == 333:
        return 'o'
    if (ord(str(board[0])) and ord(str(board[4])) and ord(str(board[8]))) == 360:
        return 'x'
    if (ord(str(board[0])) and ord(str(board[4])) and ord(str(board[8]))) == 333:
        return 'o'
    return False


def play(board):

    while not game_over(board):
        print_board(board)
        player_num = 0
        for player in range(2):
            if player_num == 0:
                position = eval(input("x's choose their position: "))
                if is_legal(board, position):
                    fill_spot(board, position, 'x')
                    print_board(board)
                    if get_winner(board) == 'x':
                        print("x wins!!!!")
                        break
            if player_num == 1:
                position = eval(input("o's choose their position: "))
                if is_legal(board, position):
                    fill_spot(board, position, 'o')
                    print_board(board)
                    if get_winner(board) == 'o':
                        print("o wins!!!!")
                        break
            player_num = player_num + 1


def main():
    user_input = "y"
    while user_input[0] == 'y':
        board = build_board()
        play(board)
        user_input = input("do you want to play again? ")
        user_input = user_input.lower()


if __name__ == '__main__':
    main()
