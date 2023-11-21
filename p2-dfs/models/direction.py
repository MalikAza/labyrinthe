from abc import ABC

class Direction(ABC):
    NORTH = 'N'
    EAST = 'E'
    WEST = 'W'
    SOUTH = 'S'
    VALID = [NORTH, EAST, WEST, SOUTH]