#!/user/bin/env python3

from brain_games.greeting_ask_user import greeting_user, ask_user
from brain_games.games.prime_game import prime_num


def main():
    attempts = 0
    user_name = greeting_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while attempts < 3:
        prime = prime_num()
        answer = ask_user(user_name, prime)
        attempts += 1
        if answer:
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
