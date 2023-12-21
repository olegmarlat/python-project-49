from random import randint, choice


GAME_TASK = 'What number is missing in the progression?'


def create_progression():
    number_start = randint(2, 9)
    length = randint(5, 10)
    number_diff = randint(1, 8)
    number_end = number_start + (length - 1) * number_diff + 1
    progression = list(range(number_start, number_end, number_diff))
    return progression


def get_game():
    progression, correct_answer, hidden_index = create_progression()
    hidden_index = progression.index(choice(progression))
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join([str(n) for n in progression])
    return question, str(correct_answer)
