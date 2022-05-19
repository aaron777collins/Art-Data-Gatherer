import numpy as np

from coordinate import Coordinate


class ScreenConverter:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def convertVectorToScreenCoordinates(self, vector: np.array):
        return Coordinate(
            ((self.width / 2) * vector[0]) + (self.width/2),
            ((self.height / 2) * vector[1]*-1) + (self.height/2))
