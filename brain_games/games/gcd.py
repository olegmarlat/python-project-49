from random import randint
import math


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def get_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    question = f'{number1} {number2}'
    correct_answer = math.gcd(number1, number2)
    return question, str(correct_answer)
