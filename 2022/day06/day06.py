"""
https://adventofcode.com/2022/day/5
"""

from collections import deque

FILE_PATH = r'./input.txt'


def find_marker(file_path: str) -> int:
    with open(file_path) as file:
        buffer = deque(file.read(1))
        pos = 1
        while len(buffer) < 4:
            pos += 1
            next_char = file.read(1)
            while next_char in buffer:
                buffer.popleft()
            buffer.append(next_char)
        return pos


def q6a():
    return find_marker(FILE_PATH)


if __name__ == '__main__':
    print(f'{q6a()=}')