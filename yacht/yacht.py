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
from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = lambda dice : 50 if dice.count(dice[0]) == len(dice) else 0
ONES = lambda dice : dice.count(1)
TWOS = lambda dice : 2*dice.count(2)
THREES = lambda dice : 3*dice.count(3)
FOURS = lambda dice : 4*dice.count(4)
FIVES = lambda dice : 5*dice.count(5)
SIXES = lambda dice : 6*dice.count(6)
FULL_HOUSE = lambda dice : sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0
FOUR_OF_A_KIND = lambda dice : 4*next(key for key, value in Counter(dice).items() if value >= 4) if max(Counter(dice).values()) >= 4 else 0
LITTLE_STRAIGHT = lambda dice : 30 if dice == list(range(1, 6)) else 0
BIG_STRAIGHT = lambda dice : 30 if dice == list(range(2, 7)) else 0
CHOICE = lambda dice : sum(dice)


def score(dice, category):
    dice.sort()

    return category(dice)
