"""Tic Tac Toe"""
import sys
from typing import Literal

X, O, BLANK = 'x', 'o', ' '
BoardChar = Literal['x', 'o', ' ']

BOARD_STR = '''
 {} | {} | {} 
-----------
 {} | {} | {} 
-----------
 {} | {} | {} 
'''


class GameOver(Exception):
    """Raised when the game ends"""


def main() -> None:
    """Runs Tic Tac Toe"""
    print_instructions()

    player_1, player_2 = choose_players()

    board = [BLANK] * 9

    while True:
        try:
            play_turn(player_1, board)
            play_turn(player_2, board)
        except GameOver:
            break


def print_instructions() -> None:
    """Print instructions on game start"""
    print(
        'Welcome to Tic Tac Toe.\n'
        'Board positions are as follows:'
    )
    print_board_positions()


def print_board_positions() -> None:
    """Prints the board positions"""
    positions = range(1, 9+1)
    print(BOARD_STR.format(*positions))


def choose_players() -> tuple[BoardChar, BoardChar]:
    """Chooses the symbols for each player"""
    while True:
        try:
            input_string = input("Choose Player 1 symbol ('x' or 'o'): ")
        except KeyboardInterrupt:
            sys.exit()

        input_string = input_string.lower()

        if input_string == X:
            return X, O

        if input_string == O:
            return O, X

        print('Try again.')


def play_turn(player: BoardChar, board: list[str]) -> None:
    """Plays one turn of the game, and throws on game over"""
    print_board(board)

    player_input(player, board)

    if check_win(player, board):
        print_board(board)
        print(f'Player {player} won!')
        raise GameOver

    if check_tie(board):
        print_board(board)
        print('It\'s a tie!')
        raise GameOver


def print_board(board: list[str]) -> None:
    """Prints the board"""
    print(BOARD_STR.format(*board))


def player_input(player_char: BoardChar, board: list[str]) -> None:
    """Takes a position input from the player"""
    while True:
        try:
            position_input = input(f'{player_char}> ')
        except KeyboardInterrupt:
            sys.exit()

        if not position_input.isdigit():
            print('Try again.')
            continue

        position = int(position_input) - 1

        if position < 0 or position >= len(board):
            print(f'Choose a value between 1 and {len(board)}.')
            continue

        if board[position] != BLANK:
            print('Choose an empty cell.')
            continue

        board[position] = player_char
        break


def check_win(char: BoardChar, board: list[str]) -> bool:
    """Checks if a player has won the game"""
    rows = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
    )
    cols = (
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    )
    diags = (
        (2, 4, 6),
        (0, 4, 8),
    )

    edges = (*rows, *cols, *diags)

    for edge in edges:
        if all(board[index] == char for index in edge):
            return True

    return False


def check_tie(board: list[str]) -> bool:
    """Checks if the game was a tie"""
    return all(char != BLANK for char in board)


if __name__ == '__main__':
    main()
