def sum_of_multiples(limit, multiples):
    mults = []

    for num in multiples:
        if num == 0:
            continue
        mults += [k for k in range(0, limit) if k % num == 0]

    return sum(set(mults))
