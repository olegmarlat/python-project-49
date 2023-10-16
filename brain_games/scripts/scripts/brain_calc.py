import prompt
from random import random
import random


def math_operator(a, b, c):
    if a == "+":
        return b + c
    elif a == "-":
        return b - c
    elif a == "*":
        return b * c
    

def game_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    item = 0
    math_list = ["+", "-", "*"]
    while item < 3:
        number1 = randint(10, 20)
        number2 = randint(1, 10)
        math = random.choice(math_list)
        print(f'Question: {number1} {math} {number2}')
        join = prompt.integer('Your answer: ')
        result = math.operator(math, number1, number2)
        if result == join:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(
                f"'{join} is wrong answer ;(."
                f"Correct answer was '{result}'\nLet's "
                f"try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')
