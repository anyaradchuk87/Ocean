from valid_check import DEFAULT_IMAGE, DEFAULT_PARAMS
from cell import Cell
from coordinate import Coordinate


class Ocean:
    def __init__(self,
                 num_rows=DEFAULT_PARAMS['num_rows'],
                 num_cols=DEFAULT_PARAMS['num_cols'],
                 num_prey=DEFAULT_PARAMS['num_prey'],
                 num_predators=DEFAULT_PARAMS['num_predators'],
                 num_obstacles=DEFAULT_PARAMS['num_obstacles']):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__num_prey = num_prey
        self.__num_predators = num_predators
        self.__num_obstacles = num_obstacles
        self.__cells = []

    def get_num_pray(self):
        return self.__num_prey

    def set_num_prey(self, a_number):
        self.__num_prey = a_number

    def get_num_predators(self):
        return self.__num_predators

    def set_num_predators(self, a_number):
        self.__num_predators = a_number

    def get_num_cols(self):
        return self.__num_cols

    def get_num_rows(self):
        return self.__num_rows

    def get_num_obstacles(self):
        return self.__num_obstacles

    def set_cell_item(self, cell, offset):
        self.__cells[offset.get_row()][offset.get_col()] = cell

    def is_valid_coordinate(self, x, y):
        if x <= -1 or y <= -1:
            return False
        if x >= self.get_num_rows() or y >= self.get_num_cols():
            return False

        return True

    def add_empty_cells(self):
        for row in range(self.get_num_rows()):
            self.__cells.append([])
            for col in range(self.get_num_cols()):
                self.__cells[row].append(Cell(self, Coordinate(row, col)))
