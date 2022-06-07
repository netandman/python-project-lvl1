#!/user/bin/env python3

import prompt


def greeting_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('What is the result of the expression')
    return name


def ask_user(name, result):
    answer = prompt.string('Your answer: ')
    if result == int(answer):
        print('Correct!')
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {result}')
        print(f"Let's try again, {name}")
        return 1


if __name__ == '__main__':
    greeting_user()
