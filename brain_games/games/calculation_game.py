#!/user/bin/env python3

from random import randint
from random import choice


def calc():
    signs_list = ['+', '-', '*']
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    sing = choice(signs_list)
    print(f'Question: {number1} {sing} {number2}')
    if sing == '+':
        result = number1 + number2
    elif sing == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return result


if __name__ == '__main__':
    calc()
