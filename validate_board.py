import numpy as np
from collections import Counter

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def validate_board(board):
    board = np.array(board)

    # Validate rows and columns
    for i in range(9):
        # Validate rows
        for k, v in Counter(board[i]).items():
            if k != '.' and v > 1:
                return False

        # Validate columns
        for k, v in Counter(board[:, i]).items():
            if k != '.' and v > 1:
                return False

    # Validate boxes
    for i in range(3):
        for j in range(3):
            box = board[i * 3: i * 3 + 3, j * 3: j * 3 + 3]
            for k, v in Counter(box.reshape(1, -1)[0]).items():
                if k != '.' and v > 1:
                    return False

    return True


print(validate_board(board))
