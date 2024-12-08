import numpy as np

FILE_NAME = r'aoc2024/day04/input.txt'


def word_search(data, word):
    """ Returns the number of instances a word can be found in a letter grid """
    letters = {letter: np.array([(r, c) for r, c in zip(*np.where(data==letter))])
               for letter in word}
    directions = [np.array((i, j)) for i in range(-1, 2) for j in range(-1, 2)]
    count = 0
    for start in letters[word[0]]:
        for d in directions:
            for i, l in enumerate(word[1:], 1):
                if not (letters[l] == start + d * i).all(axis=1).any():
                    break
            else:
                count += 1
    return count


if __name__ == '__main__':
    with open(FILE_NAME) as f:
        data = [[x for x in line] for line in f.read().splitlines()]
    data = np.array(data)

    answer_4a = word_search(data, 'XMAS')
    print(f'{answer_4a=}')