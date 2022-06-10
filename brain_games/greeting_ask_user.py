#!/user/bin/env python3

import prompt


def greeting_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_user(name, result):
    y = 1
    n = 0
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        answer = 1
        y = 'yes'
        n = 'no'
    if answer == 'no':
        answer = 0
        y = 'yes'
        n = 'no'
    if y == 'yes' or n == 'no':
        if result == int(answer):
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again, {name}")
            return 1
    elif result == int(answer):
        print('Correct!')
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {result}')
        print(f"Let's try again, {name}")
        return 1


if __name__ == '__main__':
    greeting_user()
