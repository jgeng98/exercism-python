def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError(f"You can't slice a string of length {len(series)} into slices of length {length}.")

    slices = [series[digit:digit+length] for digit in range(0, len(series)-(length-1))]

    return slices
