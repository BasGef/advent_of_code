import numpy as np

FILE_PATH = r'./input.txt'


class CathodeRayTube:
    def __init__(self, start_value=1, screen_size=(6, 40)):
        self._register = start_value
        self.signal_strength = []
        self._cycle = 0
        self.screen_x = screen_size[1]
        self._display = np.zeros(screen_size, str)

    def check_cycle(self):
        if self._cycle % 40 != 20:
            return
        self.signal_strength.append(self._register * self._cycle)

    def noop(self):
        self._cycle += 1
        self.check_cycle()
        self.draw()

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

    def draw(self):
        y, x = divmod(self._cycle - 1, self.screen_x)
        pixel = '#' if abs(x - self._register) <= 1 else ' '
        self._display[y][x] = pixel

    @property
    def display(self):
        return '\n'.join([''.join(line) for line in self._display])


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def q10():
    crt = CathodeRayTube()
    for command in load_data(FILE_PATH):
        crt.do_command(command)
    q10a = sum(crt.signal_strength)
    print(f'{q10a=}')
    print('q10b=\n' + crt.display)


if __name__ == '__main__':
    q10()
