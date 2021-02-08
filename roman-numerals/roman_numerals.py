def roman(number):
    if number > 3000:
        raise ValueError("The Romans only counted up to 3000.")

    thousands = {3: "MMM", 2: "MM", 1: "M"}

    hundreds = {
        9: "CM",
        8: "DCCC",
        7: "DCC",
        6: "DC",
        5: "D",
        4: "CD",
        3: "CCC",
        2: "CC",
        1: "C",
        0: "",
    }

    tens = {
        9: "XC",
        8: "LXXX",
        7: "LXX",
        6: "LX",
        5: "L",
        4: "XL",
        3: "XXX",
        2: "XX",
        1: "X",
        0: "",
    }

    ones = {
        9: "IX",
        8: "VIII",
        7: "VII",
        6: "VI",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I",
        0: "",
    }

    translations = [ones, tens, hundreds, thousands]

    roman_num = ""

    for k in range(len(str(number))):
        roman_num = translations[k].get(number % 10) + roman_num

        number = number // 10

    return roman_num
