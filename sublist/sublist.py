"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def is_sublist(list_one, list_two):
    for i in range(len(list_two) - len(list_one) + 1):
        if all(list_one[j] == list_two[i + j] for j in range(len(list_one))):
            return True
    return False


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if len(list_one) < len(list_two) and is_sublist(list_one, list_two):
        return SUBLIST

    if len(list_one) > len(list_two) and is_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL
