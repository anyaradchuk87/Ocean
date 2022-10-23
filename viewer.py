from coordinate import Coordinate
from cell import Cell

class Viewer:
    def __init__(self, ocean):
        self.ocean = ocean

    @staticmethod
    def show_message(text):
        print(text)

    def show_stat(self, iteration):
        print(f'Iteration: {iteration} - '
              f'Obstacles: {self.ocean.get_num_obstacles()} - '
              f'Predators: {self.ocean.get_num_predators()} - '
              f'Prey: {self.ocean.get_num_pray()}')

    def show_border(self):
        print('~' * (self.ocean.get_num_cols() + 4))

    def show_ocean(self):
        offset = Coordinate(0, 0)
        for row in range(self.ocean.get_num_rows()):
            offset.set_y(row)
            print('| ')  # end=' '
            for col in range(self.ocean.get_num_cols()):
                offset.set_x(col)
                print(self.ocean.get_cell_item(offset), end='')
            print(' |')

    def show_iteration(self, iteration):
        self.show_stat(iteration)
        self.show_border()
        self.show_ocean()
        self.show_border()

