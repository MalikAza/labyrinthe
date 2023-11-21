from .case import Case
from custom_types import Coordinates
from exceptions import TravelTooFast, TravelDiagonaly
from .direction import Direction

from typing import List

class Player:
    def __init__(self, start_x: int, start_y: int) -> None:
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.direction = 'S'
        self.stack : List[Coordinates] = []

    def __move_to(self, x: int, y: int):
        if x < self.x-1 or x > self.x+1:
            raise TravelTooFast
        if y < self.y-1 or y > self.y+1:
            raise TravelTooFast
        
        if x != self.x and y != self.y:
            raise TravelDiagonaly

        self.stack.append({'x': self.x, 'y': self.y})
        self.x = x
        self.y = y
        self.steps += 1

    def get_coordinates_from_direction(self, direction: str) -> Coordinates:
        if direction not in Direction.VALID:
            raise 'BadDirection'
        
        match direction:
            case Direction.SOUTH:
                return {'x': self.x, 'y': self.y+1}
            case Direction.EAST:
                return {'x': self.x+1, 'y': self.y}
            case Direction.WEST:
                return {'x': self.x-1, 'y': self.y}
            case Direction.NORTH:
                return {'x': self.x, 'y': self.y-1}

    def move_to_direction(self, direction: str):
        if direction not in Direction.VALID:
            raise 'BadDirection'
        
        coordinates = self.get_coordinates_from_direction(direction)
        self.__move_to(coordinates['x'], coordinates['y'])

    def go_backwards(self):
        coordinates = self.stack.pop()
        self.__move_to(coordinates['x'], coordinates['y'])

    def change_direction(self):
        match self.direction:
            case Direction.SOUTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.NORTH
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.WEST:
                self.direction = Direction.SOUTH

    def adjacent_cases(self, lab: 'Labyrinthe') -> List['AdjacentCase']:
        if (self.y-1) < 0: north_case = Case.fake_wall().format_to_adjacent(Direction.NORTH)
        else: north_case = lab.board[self.x][self.y-1].format_to_adjacent(Direction.NORTH)

        if (self.y+1) > lab.max_index_y: south_case = Case.fake_wall().format_to_adjacent(Direction.SOUTH)
        else: south_case = lab.board[self.x][self.y+1].format_to_adjacent(Direction.SOUTH)

        if (self.x+1) > lab.max_index_x: east_case = Case.fake_wall().format_to_adjacent(Direction.EAST)
        else: east_case = lab.board[self.x+1][self.y].format_to_adjacent(Direction.EAST)

        if (self.x-1) < 0: west_case = Case.fake_wall().format_to_adjacent(Direction.WEST)
        else: west_case = lab.board[self.x-1][self.y].format_to_adjacent(Direction.WEST)

        return [north_case, south_case, east_case, west_case]
    
    def get_coordinates(self) -> Coordinates:
        return {
            'x': self.x,
            'y': self.y
        }