from functools import cache

FILE_NAME = r'aoc2024/day22/input.txt'


@cache
def next_number(number):
    number = (64 * number) ^ number
    number = number % 16777216
    number = (number // 32) ^ number
    number = number % 16777216
    number = (2048 * number) ^ number
    number = number % 16777216
    return number


def read_data():
    with open(FILE_NAME) as f:
        data = list(map(int, f.read().splitlines()))
    return data


if __name__ == '__main__':
    new_numbers = read_data()
    for _ in range(2000):
        new_numbers = [next_number(n) for n in new_numbers]

    answer_22a = sum(new_numbers)
    print(answer_22a)