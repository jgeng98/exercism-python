import numpy as np


def axis_extrema(matrix, axis, function):
    extrema = []
    # transpose so correct axis is first
    transposition_list = [1, 0]
    transposition_list = transposition_list[axis:] + transposition_list[:axis]
    matrix = np.transpose(matrix, transposition_list)
    for i, row in enumerate(matrix):
        extrema = extrema + [(i, col) for col in np.where(row == function(row))[0]]
    if axis == 0:
        extrema = [(y, x) for (x, y) in extrema]
    return extrema


def saddle_points(matrix):
    matrix = np.array(matrix)

    if matrix.dtype == np.dtype("O"):
        raise ValueError("The matrix is not rectangular.")

    if matrix.size == 0:
        return []

    saddle_points = set(axis_extrema(matrix, 1, np.max)) & set(
        axis_extrema(matrix, 0, np.min)
    )

    return [{"row": row + 1, "column": col + 1} for row, col in saddle_points]
