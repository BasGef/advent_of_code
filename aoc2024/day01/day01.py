from collections import Counter

FILE_PATH = r'./aoc2024/day01/input.txt'


def process_lists():
    with open(FILE_PATH) as f:
        locations = f.read().splitlines()
    locations = [map(int, l.split()) for l in locations]
    locs1, locs2 = zip(*locations)
    return locs1, locs2


def distance(list1, list2): # 1a
    list1 = sorted(list1)
    list2 = sorted(list2)
    return sum(abs(l1 - l2) for l1, l2 in zip(list1, list2))


def similarity(list1, list2): # 1b
    count = Counter(list2)
    return sum(l * count[l] for l in list1)


if __name__ == '__main__':
    locs1, locs2 = process_lists()
    answer_1a = distance(locs1, locs2)
    answer_1b = similarity(locs1, locs2)

    print(f'{answer_1a=}')
    print(f'{answer_1b=}')
