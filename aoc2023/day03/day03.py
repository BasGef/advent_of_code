from __future__ import annotations

from typing import List
import re

FILE_PATH = './input.txt'


class Coordinate:
    def __init__(self, y: int, x_min: int, x_max: int | None = None,
                 value: str | int | None = None):
        self.y = y
        self.x_min = x_min
        self.x_max = x_max or x_min
        self.value = value

    def adjacent(self, other: Coordinate):
        if abs(self.y - other.y) > 1:
            return False
        if other.x_max < self.x_min - 1:
            return False
        if other.x_min > self.x_max + 1:
            return False
        return True


def find_gear_ratios(parts: List[Coordinate], symbols: List[Coordinate]):
    for symbol in symbols:
        if symbol.value != '*':
            continue
        adjacent = [part for part in parts if part.adjacent(symbol)]
        if len(adjacent) != 2:
            continue
        yield adjacent[0].value * adjacent[1].value


if __name__ == '__main__':
    with open(FILE_PATH) as f:
        grid = f.read().splitlines()

        parts = [Coordinate(y, match.start(), match.end()-1, int(match.group()))
                 for y, row in enumerate(grid)
                 for match in re.finditer(r'\d+', row)]
        symbols = [Coordinate(y, match.start(), match.end()-1, match.group())
                   for y, row in enumerate(grid)
                   for match in re.finditer(r'[^0-9.]', row)]

        # TODO: this is inefficient; we could improve by only searching those
        #       symbols that have row-adjacency. Requires redesign of above
        answer_3a = sum(part.value for part in parts if
                        any(part.adjacent(symbol) for symbol in symbols))
        answer_3b = sum(find_gear_ratios(parts, symbols))

        print(f'{answer_3a=}')
        print(f'{answer_3b=}')