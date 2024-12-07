"""
https://adventofcode.com/2022/day/4
"""

from typing import List, Tuple

FILE_PATH = r'./input.txt'


def load_data(file_path: str) -> List[str]:
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def range_from_string(string: str):
    return tuple(int(v) for v in string.split('-'))


def is_subset(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    """
    Checks if either range fully overlaps the other
    Note: assumes ranges are correctly specified as [Min, Max]
    """
    return (range1[0] - range2[0]) * (range2[1] - range1[1]) >= 0


def overlaps(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    """
    Checks if the two ranges overlap partially
    Note: assumes ranges are correctly specified as [Min, Max]
    """
    return not (range1[0] > range2[1] or range2[0] > range1[1])


def q4a() -> int:
    data = load_data(FILE_PATH)
    data = [tuple(range_from_string(r) for r in pair.split(',')) for pair in data]
    return sum(is_subset(*r) for r in data)


def q4b() -> int:
    data = load_data(FILE_PATH)
    data = [tuple(range_from_string(r) for r in pair.split(',')) for pair in data]
    return sum(overlaps(*r) for r in data)


if __name__ == '__main__':
    print(f'{q4a()=}')
    print(f'{q4b()=}')