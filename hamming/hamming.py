def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The two DNA strands must be of the same length.')
    differences = 0
    index = 0
    for i in strand_a:
        if i != strand_b[index]:
            differences += 1
        index += 1
    return differences