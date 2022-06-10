#!/user/bin/env python

import prompt
from random import randint


def greeting_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    attempts = 0
    user = greeting_user()
    while attempts < 3:
        number = randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                attempts += 1
            else:
                print(f'{answer} is wrong answer ;(. Correct answer was "no".')
                break
        elif number % 2 != 0:
            if answer == 'no':
                print('Correct!')
                attempts += 1
            else:
                print(f'{answer} is wrong answer ;(. Correct answer was "yes".')
                break
    else:
        print(f'Congratulations, {user}!')
    return


if __name__ == '__main__':
    main()
