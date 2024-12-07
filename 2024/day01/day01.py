FILE_PATH = r'./2024/day01/input.txt'

if __name__ == '__main__':
    with open(FILE_PATH) as f:
        locations = f.read().splitlines()

    locations = [map(int, l.split()) for l in locations]

    locs1, locs2 = zip(*locations)
    locs1 = sorted(locs1)
    locs2 = sorted(locs2)

    answer_1a = sum(abs(l1 - l2) for l1, l2 in zip(locs1, locs2))
    print(f'{answer_1a=}')
