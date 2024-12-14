from collections import deque
import itertools

FILE_NAME = r'aoc2024/day09/input.txt'


def read_diskmap():
    with open(FILE_NAME) as f:
        data = f.read()
    data = ([None if i % 2 else i // 2] * int(d) for i, d in enumerate(data))
    data = deque(itertools.chain.from_iterable(data))
    return data


def compact_disk(disk_map):  # or should this be called fragment files?
    disk_map = disk_map.copy()
    cursor = 0
    checksum = 0
    while disk_map:
        file_id = disk_map.popleft()
        while file_id is None:
            file_id = disk_map.pop()
        checksum += cursor * file_id
        cursor += 1
    return checksum


if __name__ == '__main__':
    disk_map = read_diskmap()
    answer_9a = compact_disk(disk_map)
    print(f'{answer_9a=}')

