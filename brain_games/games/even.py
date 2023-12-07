from random import randint
''' Generate'''

DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def game_flow():
    item = 0
    while item < 3:
        question = randint(1, 999999)
        if question % 2 == 0:
            return "yes"
        else:
            return "no"
