#!/user/bin/env python3

from brain_games.greeting_ask_user import greeting_user, ask_user
from brain_games.games.progress_game import arithmetic_progr


def main():
    attempts = 0
    user_name = greeting_user()
    print('What number is missing in the progression?')
    while attempts < 3:
        a_progr = arithmetic_progr()
        answer = ask_user(user_name, a_progr)
        attempts += 1
        if answer:
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
