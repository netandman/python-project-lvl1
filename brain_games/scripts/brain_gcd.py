#!/user/bin/env python3

from brain_games.greeting_ask_user import greeting_user, ask_user
from brain_games.games.gcd_game import gcd


def main():
    attempts = 0
    user_name = greeting_user()
    print('Find the greatest common divisor of given numbers.')
    while attempts < 3:
        devisor = gcd()
        answer = ask_user(user_name, devisor)
        attempts += 1
        if answer:
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
