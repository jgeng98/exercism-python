def zero_to_ninetynine(number):
    if number < 0 or number > 99:
        raise ValueError("The number you entered is outside the allowed range.")

    words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if number < 20:
        return words.get(number)
    elif number % 10 == 0:
        return words.get(number)
    else:
        return "-".join([words.get(number - number % 10), words.get(number % 10)])


def break_into_thousands(number):
    if number < 1000:
        raise ValueError("The number you entered is outside the allowed range.")

    nums = []

    while number > 0:
        nums.append(number % 1000)
        number //= 1000

    return nums


def hundreds(number):
    if len(str(number)) == 1 or len(str(number)) == 2:
        return zero_to_ninetynine(number)
    elif number % 100 == 0:
        return zero_to_ninetynine(int(str(number)[0])) + " hundred"
    else:
        return (
            zero_to_ninetynine(int(str(number)[0]))
            + " hundred "
            + zero_to_ninetynine(int(str(number)[1:3]))
        )


def insert_scale_word(list_of_thousands):
    if len(list_of_thousands) > 4:
        raise ValueError("The number you entered is outside the allowed range.")

    scales = {0: "", 1: " thousand", 2: " million", 3: " billion"}
    scaled = []

    for i in range(0, len(list_of_thousands)):
        if list_of_thousands[i] == 0:
            continue
        scaled.append(hundreds(list_of_thousands[i]) + scales.get(i))

    scaled.reverse()

    return " ".join(scaled)


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Please enter a number between 0 and 999,999,999,999.")

    if number < 100:
        return zero_to_ninetynine(number)
    elif number < 1000:
        return hundreds(number)
    else:
        return insert_scale_word(break_into_thousands(number))
