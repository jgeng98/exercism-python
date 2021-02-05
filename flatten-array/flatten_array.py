def flatten(iterable):
    flat = []

    for l in iterable:
        if type(l) is list:
            flat.extend(flatten(l))
        else:
            flat.append(l)

    return [k for k in flat if k is not None]
