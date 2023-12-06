from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_flow():
    item = 0
    while item < 3:
        number = randint(1, 999999999)
        question = ('{number}')
        if number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
    return question, correct_answer
