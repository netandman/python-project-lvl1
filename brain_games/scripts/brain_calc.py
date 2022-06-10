#!/user/bin/env python3

from brain_games.greeting_ask_user import greeting_user, ask_user
from brain_games.games.calculation_game import calc


def main():
    attempts = 0
    user_name = greeting_user()
    print('What is the result of the expression')
    while attempts < 3:
        result_calc = calc()
        answer = ask_user(user_name, result_calc)
        attempts += 1
        if answer:
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
