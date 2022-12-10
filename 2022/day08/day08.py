import numpy as np

FILE_PATH = r'./input.txt'

def load_data(file_path):
    with open(file_path) as file:
        data = np.array([[int(c) for c in line] for line in file.read().splitlines()])
    return data


# TODO: there must be a more efficient way to compute rolling maximum
def rolling_max(vector):
    return [max(vector[:i+1]) for i in range(len(vector))]


def get_sightline(array, rotation=0):
    sightline = np.apply_along_axis(rolling_max, 1, np.rot90(array, rotation))
    sightline = np.pad(sightline, ((0, 0), (1, 0)), constant_values=-1)[:, :-1]
    return np.rot90(sightline, -rotation)


def count_visible_trees(array):
    sightlines = [get_sightline(array, r) for r in range(4)]
    visibility = np.array(sightlines).min(axis=0)
    return (array > visibility).sum()


def q8a():
    data = load_data(FILE_PATH)
    return count_visible_trees(data)

if __name__ == '__main__':
    print(f'{q8a()=}')
