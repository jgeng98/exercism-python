import math


def factors(value):
    primes = []

    while value % 2 == 0:
        primes.append(2)
        value /= 2

    for i in range(3, int(math.sqrt(value)) + 1, 2):
        while value % i == 0:
            primes.append(i)
            value /= i

    if value > 2:
        primes.append(value)

    return primes

