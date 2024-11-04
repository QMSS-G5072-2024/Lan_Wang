
import pytest

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, player):
    if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == ' ':
            board[row][col] = player
            return True
    return False

def check_winner(board):
    lines = board + list(zip(*board))
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if all(cell == 'X' for cell in line):
            return 'X'
        if all(cell == 'O' for cell in line):
            return 'O'
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

def reset_game():
    return initialize_board()

@pytest.fixture
def fresh_board():
    return initialize_board()

@pytest.mark.parametrize("initial_board, row, col, player, expected_result, expected_board", [
    ([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'X', True, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'O', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 1, 1, 'O', True, [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 3, 0, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 3, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], -1, 0, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
])
def test_make_move(initial_board, row, col, player, expected_result, expected_board):
    result = make_move(initial_board, row, col, player)
    assert result == expected_result
    assert initial_board == expected_board
