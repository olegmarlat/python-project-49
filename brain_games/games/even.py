from random import randint
''' Generate'''

DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def game_flow():
    item = 0
    while item < 3:
        question = randint(1, 999999)
        return "yes" if question % 2 == 0 else "no"
