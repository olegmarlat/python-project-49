from random import randint


GAME_TASK = 'What number is missing in the progression?'


def game_progression():
    item = 0
    while item < 3:
        number1 = randint(1, 10)
        number2 = randint(100, 150)
        num_progr = randint(1, 8)
        numbers = []
        for i in range(number1, number2, num_progr):
            numbers.append(i)
        number1 = randint(0, 9)
        correct_answer = numbers[number1]
        numbers[number1] = '..'
        question = " ".join(map(str, numbers[0:10]))
        print(f'Question: {question}')
    return question, correct_answer
