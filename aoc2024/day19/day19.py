from functools import cache

FILE_NAME = r'aoc2024/day19/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    patterns = set(data[0].split(', '))
    designs = data[2:]
    return patterns, designs


def design_is_possible(design, patterns):
    if design == '':
        return True

    max_len = min(len(design), len(max(patterns, key=len)))
    for i in range(1, max_len + 1):
        if design[:i] not in patterns:
            continue
        if design_is_possible(design[i:], patterns):
            return True
    return False


@cache
def count_options(design, patterns):
    if design == '':
        return 1
    return sum(count_options(design.removeprefix(p), patterns) for p in patterns.split(',') if design.startswith(p))


if __name__ == '__main__':
    patterns, designs = read_data()

    possible_designs = [d for d in designs if design_is_possible(d, patterns)]
    answer_19a = len(possible_designs)
    print(f'{answer_19a}')

    pattern_string = ','.join(patterns) # OK, back to str for hashing and caching
    answer_19b = sum(count_options(d, pat) for d in possible_designs)
    print(f'{answer_19b}')
