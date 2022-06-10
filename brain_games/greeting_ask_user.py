#!/user/bin/env python3

import prompt


def greeting_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_user(name, result):
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        answer = 1
        y = 'yes'
    if answer == 'no':
        answer = 0
        n = 'no'
    if result == int(answer):
        print('Correct!')
    else:
        if y:
            n = 'no'
            print(f'{y} is wrong answer ;(. Correct answer was {n}')
            print(f"Let's try again, {name}")
            return 1
        elif n:
            y = 'yes'
            print(f'{n} is wrong answer ;(. Correct answer was {y}')
            print(f"Let's try again, {name}")
            return 1
        print(f'{answer} is wrong answer ;(. Correct answer was {result}')
        print(f"Let's try again, {name}")
        return 1


if __name__ == '__main__':
    greeting_user()
