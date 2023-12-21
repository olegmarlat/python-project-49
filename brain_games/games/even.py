from random import randint
''' Generate'''

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    question = randint(1, 99)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer
