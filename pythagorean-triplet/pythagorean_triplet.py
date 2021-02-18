def is_pythagorean(num1, num2, num3):
    return num1 ** 2 + num2 ** 2 == num3 ** 2


def triplets_with_sum(number):
    triplets = []

    for i in range(1, number // 3):
        for j in range(i + 1, (number - i) // 2 + 1):
            if is_pythagorean(i, j, number - i - j):
                triplets.append([i, j, number - i - j])

    return triplets
