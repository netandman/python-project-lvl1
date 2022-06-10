#!/user/bin/env python3

from random import randint


def prime_num():
    num = randint(2, 100)
    print(f'Question: {num}')
    dev_num = 1
    if num != 2:
        while dev_num < num:
            dev_num += 1
            result = num % dev_num
            if dev_num == num:
                return 1
            if result == 0:
                return 0
    return 1


if __name__ == "__main__":
    prime_num()
