def score(word):
    one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two_points = ['D', 'G']
    three_points = ['B', 'C', 'M', 'P']
    four_points = ['F', 'H', 'V', 'W', 'Y']
    five_points = ['K']
    eight_points = ['J', 'X']
    ten_points = ['Q', 'Z']

    total = 0

    for letter in word:
        if letter.upper() in one_point:
            total += 1
        if letter.upper() in two_points:
            total += 2
        if letter.upper() in three_points:
            total += 3
        if letter.upper() in four_points:
            total += 4
        if letter.upper() in five_points:
            total += 5
        if letter.upper() in eight_points:
            total += 8
        if letter.upper() in ten_points:
            total += 10
    
    return total