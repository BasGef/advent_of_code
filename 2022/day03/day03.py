"""
https://adventofcode.com/2022/day/3
"""

FILE_PATH = r'./input.txt'

def load_data(file_path: str):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def split_in_half(s):
    return s[:len(s)//2], s[len(s)//2:]


def get_duplicates(s1, s2):
    return {s for s in s1 if s in s2}


def get_values(chars):
    # values: a-z = 1-26; A-Z=27-52
    # this is like ord() but with offset -38 (64+26) for lcase and -96 for ucase
    return sum(ord(c) - (38 if ord(c) < 91 else 96) for c in chars)

def q3a():
    data = load_data(FILE_PATH)
    data = [split_in_half(line) for line in data]
    duplicates = [get_duplicates(*d) for d in data]
    return sum(get_values(d) for d in duplicates)

if __name__ == '__main__':
    print(f'{q3a()=}')


