FILE_PATH = r'./input.txt'


class Clock:
    def __init__(self, start_value=1):
        self._register = start_value
        self.signal_strength = []
        self._cycle = 0

    def check_cycle(self):
        if self._cycle % 40 != 20:
            return
        self.signal_strength.append(self._register * self._cycle)

    def noop(self):
        self._cycle += 1
        self.check_cycle()

    def add(self, value):
        self.noop()
        self.noop()
        self._register += value

    def do_command(self, command):
        if command == 'noop':
            self.noop()
        else:
            value = int(command.split(' ')[1])
            self.add(value)


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def q10a():
    clock = Clock()
    for command in load_data(FILE_PATH):
        clock.do_command(command)
    return sum(clock.signal_strength)


if __name__ == '__main__':
    print(f'{q10a()=}')