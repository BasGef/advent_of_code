import itertools

FILE_PATH = r'./aoc2024/day02/input.txt'


def read_data():
    with open(FILE_PATH, 'r') as f:
        data = f.read().splitlines()
    data = [list(map(int, d.split())) for d in data]
    return data


def validate_report(report, max_diff=3):
    diffs = {y - x for x, y in itertools.pairwise(report)}
    if min(diffs) <= 0 <= max(diffs):
        return 0
    if min(diffs) < -max_diff or max(diffs) > max_diff:
        return 0
    return 1


def validate_report_dampened(report, max_diff=3, max_errors=1):
    desc = report[2] < report[1] if report[1] == report[0] else report[1] < report[0]
    errors = 0
    for x, y in itertools.pairwise(report):
        if x == y or (y < x) ^ desc or abs(y - x) > max_diff:
            errors += 1
            if errors > max_errors:
                return 0
    return 1


if __name__ == '__main__':
    data = read_data()
    answer_2a = sum(validate_report(report) for report in data)
    answer_2b = sum(validate_report_dampened(report) for report in data)

    print(f'{answer_2a=}')
    print(f'{answer_2b=}')

