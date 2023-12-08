from random import randint
''' Generate'''

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_flow():
    number = randint(1, 99)
    question = {number}
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
