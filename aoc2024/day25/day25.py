FILE_NAME = r'aoc2024/day25/input.txt'


def read_data():
    keys = []
    locks = []

    with open(FILE_NAME) as f:
        data = f.read().split('\n\n')
    lock_height = len(data[0].splitlines())
    for lock_key in data:
        heights = [''.join(x).count('#') for x in zip(*lock_key.splitlines())]
        (locks if lock_key[0] == '#' else keys).append(heights)
    return keys, locks, lock_height


if __name__ == '__main__':
    keys, locks, lock_height = read_data()
    combinations = [(lock, key) for lock in locks for key in keys]
    matches = [all(sum(c) <= 7 for c in zip(*combination)) for combination in combinations]
    answer_25a = sum(matches)
    print(f'{answer_25a}')
