from prey import Prey
from valid_check import DEFAULT_IMAGE


class Predator(Prey):
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Predator'],
                 time_to_reproduce=6, time_to_feed=6):
        Prey.__init__(self, ocean, offset, image, time_to_reproduce)
        self.__time_to_feed = time_to_feed

    def get_time_to_feed(self):
        return self.__time_to_feed

    def set_time_to_feed(self, time_to_feed):
        self.__time_to_feed = time_to_feed
