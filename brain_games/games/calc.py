import random
from random import randint


GAME_TASK = 'What is the result of the expression?'


def math_operator(operand, number1, number2):
    if operand == "+":
        return number1 + number2
    elif operand == "-":
        return number1 - number2
    elif operand == "*":
        return number1 * number2


def game_flow():
    math_list = ["+", "-", "*"]
    number1 = randint(10, 20)
    number2 = randint(1, 10)
    math = random.choice(math_list)
    question = f"{number1} {math} {number2}"
    correct_answer = math_operator(math, number1, number2)
    return question, correct_answer
