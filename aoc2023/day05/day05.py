from typing import List, Dict, Tuple
import re
import itertools

FILE_PATH = './test_input.txt'


class Almanac:
    def __init__(self, data: str):
        seeds, *maps = data.split('\n\n')
        self.seeds = [int(seed) for seed in re.findall(r'\d+', seeds)]
        self.mappings = dict(parse_mapping(m) for m in maps)

    def solve_map(self, target: str) -> Tuple[int,]:
        start = 'seed'
        values = self.seeds
        # this assumes each start map only has one next step
        # it also does not check for circular mappings -> inf loop
        paths = dict(self.mappings.keys())

        while start != target:
            if start not in paths.keys():
                raise ValueError('cannot compute next for {start}')
            step = (start, paths[start])

            values = [_map_value(self.mappings[step], value) for value in
                      values]
            start = paths[start]
        return values


def _map_value(mapping, value):
    for entry in mapping:
        if entry.includes(value):
            return entry.convert(value)
    return value


class MapEntry:
    def __init__(self, target: int, source: int, range_len: int):
        self.start = source
        self.end = source + range_len
        self.target = target

    def convert(self, number: int) -> int:
        return self.target - self.start + number

    def includes(self, number: int) -> bool:
        return self.start <= number <= self.end


class SeedRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'SeedRange({self.start}, {self.end})'


def parse_name(text: str) -> Tuple[str, str]:
    return re.match('(\w+)-to-(\w+)', text).groups()


def parse_mapping(mapping: List[str]) -> Tuple[Tuple, Dict]:
    name, *data = mapping.splitlines()
    name = parse_name(name)
    full_map = {MapEntry(*map(int, entry.split())) for entry in data}
    return name, full_map


if __name__ == '__main__':
    with open(FILE_PATH) as f:
        almanac = Almanac(f.read())

    answer_5a = min(almanac.solve_map('location'))
    print(f'{answer_5a=}')

    seed_ranges = [SeedRange(s, r) for s,r in itertools.pairwise(almanac.seeds)][::2]
    # solve for ranges
    start = 'seed'
    paths = dict(almanac.mappings.keys())
    while start != target:
        if start not in paths.keys():
            raise ValueError('cannot compute next for {start}')
        cur_map = almanac.mappings[(start, paths[start])]
        for m in cur_map:
            for



    # for part b, we need to figure this out for ranges
    # backsolve for paths
    paths = list(almanac.mappings.keys())
    final_destination = 'location'

    # step N = 'humidity'->'location'
    mmap = [(m.start, m.stop) for m in almanac.mappings[('humidity', 'location')]
