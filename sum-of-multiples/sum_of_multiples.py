def sum_of_multiples(limit, multiples):
    mults = []

    for num in multiples:
        if num == 0:
            continue
        mults += [k for k in range(num, limit, num)]

    return sum(set(mults))
