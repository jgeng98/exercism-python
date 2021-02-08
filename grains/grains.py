def square(number):
    if number < 1 or number > 64:
        raise ValueError(
            f"It doesn't make sense to calculate the number of grains given on square {number} of a 64-square chessboard."
        )
    return 2 ** (number - 1)


def total():
    return sum([2 ** i for i in range(64)])
