"""
https://adventofcode.com/2022/day/3
"""

from itertools import islice
from typing import Iterable, Any, Tuple, Set, List

FILE_PATH = r'./input.txt'

def load_data(file_path: str) -> List[str]:
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def split_in_half(s: str) -> Tuple[str, str]:
    return s[:len(s)//2], s[len(s)//2:]


def get_duplicates(s1: str, s2: str) -> Set:
    return {s for s in s1 if s in s2}


def get_values(chars: Iterable) -> int:
    # values: a-z = 1-26; A-Z=27-52
    # this is like ord() but with offset -38 (64+26) for lcase and -96 for ucase
    return sum(ord(c) - (38 if ord(c) < 91 else 96) for c in chars)


def q3a() -> int:
    data = load_data(FILE_PATH)
    data = [split_in_half(line) for line in data]
    duplicates = [get_duplicates(*d) for d in data]
    return sum(get_values(d) for d in duplicates)


def triplewise(it: Iterable) -> Any:
    for item in zip(islice(it, 0, None, 3), islice(it, 1, None, 3),
                    islice(it, 2, None, 3)):
        yield item

def q3b():
    data = load_data(FILE_PATH)
    data = [set(line) for line in data]
    unique = [t[0].intersection(t[1], t[2]) for t in triplewise(data)]
    return get_values(''.join(u.pop() for u in unique))

if __name__ == '__main__':
    print(f'{q3a()=}')
    print(f'{q3b()=}')



