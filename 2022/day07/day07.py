from __future__ import annotations

from file import File
from folder import Folder

FILE_PATH = r'./input.txt'


def parse_ls_output(string):
    description, name = string.split()
    if description == 'dir':
        return Folder(name)
    return File(name, int(description))


def load_file_tree(file_path):
    root = Folder('/')
    cur_dir = root
    with open(file_path) as file:
        terminal_history = file.read().splitlines()
    for line in terminal_history:
        # ls output
        if not line.startswith('$'):
            obj = parse_ls_output(line)
            cur_dir.append(obj)
            continue
        # instructions
        if line == '$ ls':
            continue
        if line == '$ cd ..':
            cur_dir = cur_dir.parent
            continue
        if line == '$ cd /':
            cur_dir = root
            continue
        *_, name = line.split(' ')
        cur_dir = cur_dir[name]
    return root


def find_small_folders(node, max_size):
    folders = []
    for item in node:
        if isinstance(item, File):
            continue
        if item.size <= max_size:
            folders.append(item)
        folders.extend(find_small_folders(item, max_size))
    return folders


def q7a():
    tree = load_file_tree(FILE_PATH)
    folders = find_small_folders(tree, 100_000)
    return sum(f.size for f in folders)


if __name__ == '__main__':
    print(f'{q7a()=}')