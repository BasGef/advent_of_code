FILE_PATH = r'./input.txt'

def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data

def q10a():
    cycle = 0
    register= []
    value = 1
    for command in load_data(FILE_PATH):
        cycle += 1
        if cycle % 40 == 20:
            register.append(cycle * value)
        if command == 'noop':
            continue
        cycle += 1
        add = int(command.split(' ')[1])
        print(add)
        if cycle % 40 == 20:
            register.append(value * cycle)
        value += add
    return sum(register)

if __name__ == '__main__':
    print(f'{q10a()=}')