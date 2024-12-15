from functools import cache
import math

FILE_NAME = r'aoc2024/day11/input.txt'


@cache
def blink(stone, times=1):
    if times <= 0:
        raise ValueError("blink at least once")
    if times == 1:
        return 1 if stone == 0 or math.floor(math.log10(stone) + 1) % 2 else 2
    if stone == 0:
        return blink(1, times-1)
    if math.floor(math.log10(stone) + 1) % 2 == 0:
        stones = divmod(stone, 10 ** (math.floor(math.log10(stone)+1) // 2))
        return sum(blink(s, times-1) for s in stones)
    return blink(stone * 2024, times-1)


def read_stone_data():
    with open(FILE_NAME) as f:
        data = f.read()
    data = list(map(int, data.split(' ')))
    return data


if __name__ == '__main__':
    stones = read_stone_data()
    answer_11a = sum(blink(s, 25) for s in stones)
    answer_11b = sum(blink(s, 75) for s in stones)

    print(f'{answer_11a=}')
    print(f'{answer_11b=}')
