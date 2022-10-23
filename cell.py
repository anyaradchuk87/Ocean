import random
from coordinate import Coordinate
from valid_check import DEFAULT_IMAGE


class Cell:
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Cell']):
        self.__ocean = ocean
        self.__image = image
        self.__offset = offset

    def __str__(self):
        return f'{self.get_image()}'

    def get_image(self):
        return self.__image

    def get_ocean(self):
        return self.__ocean

    def get_offset(self):
        return self.__offset

    def set_offset(self, offset):
        if self.get_ocean().is_valid_coordinate(offset.get_row(), offset.get_cols()):
            self.__offset = offset





    
