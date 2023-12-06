from random import randint
import math


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_flow():
    item = 0
    while item < 3:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        question = ('{number1} {number2}')
        correct_answer = math.gcd(number1, number2)
    return question, correct_answer
