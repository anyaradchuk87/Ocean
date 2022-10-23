from viewer import Viewer
from valid_check import DEFAULT_PARAMS
from ocean import Ocean


class Controller:
    def __init__(self, ocean):
        self.ocean = ocean
        self.viewer = Viewer(self.ocean)

    @staticmethod
    def create(num_rows=DEFAULT_PARAMS['num_rows'],
               num_cols=DEFAULT_PARAMS['num_cols'],
               num_prey=DEFAULT_PARAMS['num_prey'],
               num_predators=DEFAULT_PARAMS['num_predators'],
               num_obstacles=DEFAULT_PARAMS['num_obstacles']):
        ocean = Ocean(num_rows, num_cols, num_prey, num_predators, num_obstacles)
        ocean.

