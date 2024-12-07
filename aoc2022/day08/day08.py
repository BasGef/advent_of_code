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


def visible_trees_from_tree(tree, sightline):
    # min_height = 0  # TODO: checking min_height is apparently redundant!
    visible = 0
    for other_tree in sightline:
        visible += 1
        if other_tree >= tree:
            break
    return visible

# TODO: optimize 8b - dont need to check if tree is smaller than previous!
def q8b():
    data = load_data(FILE_PATH)

    # Edges will all have score 0, since the one zero edge is multiplied! Skip.
    scenic_score = 0
    for row in range(1, data.shape[0]-1):
        for col in range(1, data.shape[1] -1):
            tree = data[row, col]
            down = visible_trees_from_tree(tree, data[row+1:, col])
            right = visible_trees_from_tree(tree, data[row, col+1:])
            up = visible_trees_from_tree(tree, data[:row, col][::-1])
            left = visible_trees_from_tree(tree, data[row, :col][::-1])
            tree_score = down * right * up * left
            if tree_score > scenic_score:
                scenic_score = tree_score
    return scenic_score


if __name__ == '__main__':
    print(f'{q8a()=}')
    print(f'{q8b()=}')

