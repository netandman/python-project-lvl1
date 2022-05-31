#!/usr/bin/env python

from brain_games.cli import welcome_user

def main():
    greeting_user = welcome_user()
    print(greeting_user)

if __name__ == '__main__':
    main()
