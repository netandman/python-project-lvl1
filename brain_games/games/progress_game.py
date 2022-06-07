#!/user/bin/env python3

from random import randint, choice


def arithmetic_progr():
    attempts = 0
    a = randint(0, 100)
    step = randint(0, 10)
    length_list = randint(5, 10)
    nums_list = []
    while attempts < length_list:
        nums_list.append(a)
        a += step
        attempts += 1
    selection = choice(nums_list)
    index_num = nums_list.index(selection)
    nums_list.remove(selection)
    nums_list.insert(index_num, '..')
    q = " ".join(map(str, nums_list))
    print(f'Question: {q}')
    return selection


if __name__ == '__main__':
    arithmetic_progr()
