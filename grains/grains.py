def square(number):
    if number < 1 or number > 64:
        raise ValueError(
            f"It doesn't make sense to calculate the number of grains given on square {number} of a 64-square chessboard."
        )
    return 1 << (number - 1)


def total():
    return (1 << 64) - 1
