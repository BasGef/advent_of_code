from typing import List
import re

FILE_PATH = r'./input.txt'
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# 1A
def find_value(text: str) -> int:
    digits = re.findall(r'\d', text)
    return int(digits[0]) * 10 + int(digits[-1])


# 1B / Generalised
def extract_numbers(text: str, digits_only: bool = True) -> List[int]:
    if digits_only:
        digits = re.findall(r'\d', text)
        return [int(d) for d in digits]

    # lookahead ensures that overlapping digit strings are matched
    regex = fr"(?=(\d|{'|'.join(NUMBERS)}))"
    digits = re.findall(regex, text)
    return [int(d) if len(d) == 1 else NUMBERS.index(d) + 1 for d in digits]


def make_coordinate(digits: List) -> int:
    return digits[0] * 10 + digits[-1]


def extract_coordinate(text: str, digits_only: bool = True) -> int:
    digits = extract_numbers(text, digits_only)
    return make_coordinate(digits)


if __name__ == '__main__':
    with open(FILE_PATH) as f:
        data = f.read().splitlines()

    #answer_1a = sum(find_value(line) for line in data)
    answer_1a = sum(extract_coordinate(d) for d in data)
    answer_1b = sum(extract_coordinate(d, False) for d in data)
    print(f'{answer_1a=}')
    print(f'{answer_1b=}')