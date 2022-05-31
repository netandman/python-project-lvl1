#!/user/bin/env python
import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    result = f'Hello, {name}!'
    return result

if __name__ == '__main__':
    print(welcome_user())
