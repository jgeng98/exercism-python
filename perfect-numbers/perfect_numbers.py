import functools


def classify(number):
    if number < 1:
        raise ValueError("This classification system only works for natural numbers.")

    factors = set(
        functools.reduce(
            list.__add__,
            (
                [i, number // i]
                for i in range(1, int(number ** 0.5) + 1)
                if number % i == 0
            ),
        )
    )

    factors.remove(number)

    if sum(factors) > number:
        return "abundant"
    elif sum(factors) < number:
        return "deficient"
    else:
        return "perfect"
