import re

FILE_PATH = r'./aoc2024/day03/input.txt'

if __name__ == '__main__':
    with open(FILE_PATH, 'r') as f:
        data = f.read()

    regex = r'mul\((\d+),(\d+)\)'
    muls = re.findall(regex, data)
    answer_1a = sum(int(m[0]) * int(m[1]) for m in muls)
    print(f'{answer_1a=}')
