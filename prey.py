from cell import Cell
from valid_check import DEFAULT_IMAGE


class Prey(Cell):
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Prey'], time_to_reproduce=6):
        Cell.__init__(self, ocean, offset, image)
        self.__time_to_reproduce = time_to_reproduce

    def get_time_to_reproduce(self):
        return self.__time_to_reproduce
