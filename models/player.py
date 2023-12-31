from .case import Case
from custom_types import Coordinates
from exceptions import TravelTooFast, TravelDiagonaly
from .direction import Direction

from typing import List
from functools import cmp_to_key

class Player:
    def __init__(self, start_x: int, start_y: int) -> None:
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.visited : List[Coordinates] = []
        self.path : List[Coordinates] = []
        self.branches = []
        self.can_travel_fast = False

    def move_to(self, coordinates: Coordinates):
        x, y = coordinates['x'], coordinates['y']
        if (x < self.x-1 or x > self.x+1) and not self.can_travel_fast:
            raise TravelTooFast
        if (y < self.y-1 or y > self.y+1) and not self.can_travel_fast:
            raise TravelTooFast
        
        if (x != self.x and y != self.y) and not self.can_travel_fast:
            raise TravelDiagonaly

        self.x = x
        self.y = y
        self.steps += 1

    def go_backwards(self):
        coordinates = self.path.pop()
        self.move_to(coordinates)

    def adjacent_cases(self, lab: 'Labyrinthe') -> List['AdjacentCase']:
        if (self.y-1) < 0: north_case = Case.fake_wall()
        else: north_case = lab.board[self.x][self.y-1]
        north_case = north_case.format_to_adjacent(self, Direction.NORTH)

        if (self.y+1) > lab.max_index_y: south_case = Case.fake_wall()
        else: south_case = lab.board[self.x][self.y+1]
        south_case = south_case.format_to_adjacent(self, Direction.SOUTH)

        if (self.x+1) > lab.max_index_x: east_case = Case.fake_wall()
        else: east_case = lab.board[self.x+1][self.y]
        east_case = east_case.format_to_adjacent(self, Direction.EAST)

        if (self.x-1) < 0: west_case = Case.fake_wall()
        else: west_case = lab.board[self.x-1][self.y]
        west_case = west_case.format_to_adjacent(self, Direction.WEST)

        cases = [north_case, south_case, east_case, west_case]

        def compare(a, b):
            match a['direction']:
                case Direction.SOUTH:
                    if b['direction'] == Direction.SOUTH:
                        return 0
                    else: return -1
                
                case Direction.EAST:
                    if b['direction'] == Direction.EAST:
                        return 0
                    elif b['direction'] == Direction.SOUTH:
                        return 1
                    else: return -1

                case Direction.NORTH:
                    if b['direction'] == Direction.NORTH:
                        return 0
                    elif b['direction'] == Direction.SOUTH or b['direction'] == Direction.EAST:
                        return 1
                    else: return -1

                case Direction.WEST:
                    if b['direction'] == Direction.WEST:
                        return 0
                    else: return 1

        cases.sort(key=cmp_to_key(compare))

        return cases

    def get_coordinates(self) -> Coordinates:
        return {
            'x': self.x,
            'y': self.y
        }