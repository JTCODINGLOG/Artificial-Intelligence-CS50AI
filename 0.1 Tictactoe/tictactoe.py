"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
    if x_count <= o_count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    modified_board = []
    for row in board:
        modified_board.append(row.copy())

    modified_board[action[0]][action[1]] = player(board)
    return modified_board   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_boards = [
        # Rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Columns
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for line in winner_boards:
        a, b, c = line
        # Check if all three positions are the same (and not EMPTY)
        if board[a[0]][a[1]] != EMPTY and board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]]:
            return board[a[0]][a[1]]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True
            
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    best_action = None
    if terminal(board):
        return utility(board), best_action
    v = float("-inf")
    for action in actions(board):
        if min_value(result(board, action))[0] > v:
            v = min_value(result(board, action))[0]
            best_action = action
    return v, best_action

def min_value(board):
    best_action = None
    if terminal(board):
        return utility(board), best_action
    v = float("inf")
    for action in actions(board):
        if max_value(result(board, action))[0] < v:
            v = max_value(result(board, action))[0]
            best_action = action
    return v, best_action

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "X":
        if board == initial_state():
            return (1, 1)
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    
    
    
