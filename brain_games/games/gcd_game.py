#!/user/bin/env python3

from random import randint


def gcd():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    print(f"Question: {number1} {number2}")
    if number1 > number2:
        a = number1
        b = number2
    else:
        a = number2
        b = number1
    devision = a % b
    if devision > 0:
        while devision > 0:
            devision1 = b % devision
            if devision1 > 0:
                b = devision % devision1
            else:
                return devision
            if b > 0:
                devision = devision1 % b
            else:
                return devision1
        return b
    else:
        return b


if __name__ == '__main__':
    gcd()
