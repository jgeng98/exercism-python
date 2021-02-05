from math import prod


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError(
            f"You can't compute the product of substrings with size {size} with a string of length {len(series)}."
        )

    if size == 0:
        return 1

    slices = [
        series[digit : digit + size] for digit in range(0, len(series) - size + 1)
    ]

    slices = map(list, slices)

    slices = [list(map(int, l)) for l in slices]

    products = list(map(prod, slices))

    return max(products)
