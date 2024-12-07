"""
https://adventofcode.com/2022/day/5
"""

from collections import deque

FILE_PATH = r'./input.txt'


def find_marker(file_path: str, marker_len=4) -> int:
    with open(file_path) as file:
        buffer = deque(file.read(1))
        pos = 1
        while len(buffer) < marker_len:
            pos += 1
            next_char = file.read(1)
            while next_char in buffer:
                buffer.popleft()
            buffer.append(next_char)
        return pos


def q6a():
    return find_marker(FILE_PATH, 4)


def q6b():
    return find_marker(FILE_PATH, 14)


if __name__ == '__main__':
    print(f'{q6a()=}')
    print(f'{q6b()=}')
