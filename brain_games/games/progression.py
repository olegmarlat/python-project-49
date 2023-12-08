from random import randint


GAME_TASK = 'What number is missing in the progression?'


def game_flow():
    number1 = randint(2, 9)
    number2 = randint(100, 150)
    num_progr = randint(1, 8)
    numbers = []
    for i in range(number2):
        numbers.append(number1 + num_progr)
        number1 = randint(0, 9)
        correct_answer = numbers[number1]
        numbers[number1] = '..'
        question = " ".join(list(map(str, numbers[0:10])))
    return question, str(correct_answer)
