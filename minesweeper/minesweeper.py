import numpy as np
import re


def annotate(minefield):
    rows = len(minefield)
    if rows == 0:
        return []
    cols = len(minefield[0])
    if cols == 0:
        return [""]

    row_lengths = list(map(len, minefield))
    if row_lengths.count(row_lengths[0]) != rows:
        raise ValueError("Not a rectangular minefield.")

    if None in [re.fullmatch(r"[ \*]*", row) for row in minefield]:
        raise ValueError("Invalid characters in minefield.")

    new_board = np.empty(shape=(rows, cols), dtype=np.str_)
    for row in range(len(new_board)):
        for col in range(len(new_board[0])):
            new_board[row, col] = sum_mines(minefield, row, col)

    return list(map("".join, new_board))


def sum_mines(board, row, col):
    if board[row][col] == "*":
        return "*"

    min_row = 0 if row == 0 else row - 1
    max_row = len(board) - 1 if row == len(board) - 1 else row + 1
    min_col = 0 if col == 0 else col - 1
    max_col = len(board[0]) - 1 if col == len(board[0]) - 1 else col + 1

    sum = 0
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            sum += board[r][c] == "*"

    return " " if sum == 0 else str(sum)


if __name__ == "__main__":
    # fmt: off
    board = [" * * "]
    # fmt: on
    print(annotate(board))
