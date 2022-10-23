from cell import Cell
from valid_check import DEFAULT_IMAGE


class Obstacle(Cell):
    def __init__(self, offset, ocean, image=DEFAULT_IMAGE['Obstacle']):
        Cell.__init__(self, offset, ocean, image)
