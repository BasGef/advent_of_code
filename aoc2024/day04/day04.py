import numpy as np

FILE_NAME = r'aoc2024/day04/input.txt'


def word_search(data, word, directions=None):
    """
    Returns the starting position and direction of instances a word can be
    found in a letter grid
    """
    if directions is None:
        directions = [np.array((i, j)) for i in range(-1, 2) for j in range(-1, 2)]
    letters = {letter: np.array([(r, c) for r, c in zip(*np.where(data==letter))])
               for letter in word}
    found = []
    for start in letters[word[0]]:
        for d in directions:
            for i, l in enumerate(word[1:], 1):
                if not (letters[l] == start + d * i).all(axis=1).any():
                    break
            else:
                found.append((start, d))
    return found


def cross_words(data, word):
    """
    Searches a word grid for a word that diagonally intersects itself.
    Returns the coordinates of the each intersection.
    Word must be of odd length to avoid ambiguous results
    """
    if len(word) % 2 == 0:
        raise NotImplementedError('Words of even length are not supported')
    directions = np.array([(1, 1), (1, -1), (-1, 1), (-1, -1)])
    words = word_search(data, word, directions)
    midpoints =  np.array([origin + d * (len(word) // 2) for origin, d in words])
    unique, count = np.unique(midpoints, axis=0, return_counts=True)
    return unique[count == 2]  # >= 2, not == 2 to support palindromes


if __name__ == '__main__':
    with open(FILE_NAME) as f:
        data = [[x for x in line] for line in f.read().splitlines()]
    data = np.array(data)

    answer_4a = len(word_search(data, 'XMAS'))
    answer_4b = len(cross_words(data, 'MAS'))
    print(f'{answer_4a=}')
    print(f'{answer_4b=}')
