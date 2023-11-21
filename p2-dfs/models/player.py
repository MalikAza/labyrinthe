from .case import Case
from custom_types import Coordinates
from exceptions import TravelTooFast, TravelDiagonaly

from typing import List

class Player:
    def __init__(self, start_x: int, start_y: int) -> None:
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.direction = 'S'
        self.stack : List[Coordinates] = []

    def move_to(self, x: int, y: int):
        if x < self.x-1 or x > self.x+1:
            raise TravelTooFast
        if y < self.y-1 or y > self.y+1:
            raise TravelTooFast
        
        if x != self.x and y != self.y:
            raise TravelDiagonaly

        self.x = x
        self.y = y

    def change_direction(self):
        match self.direction:
            case 'S':
                self.direction = 'E'
            case 'E':
                self.direction = 'N'
            case 'N':
                self.direction = 'W'
            case 'W':
                self.direction = 'S'

    def adjacent_cases(self, lab: 'Labyrinthe') -> List['AdjacentCase']:
        if (self.y-1) < 0: north_case = Case.fake_wall().format_to_adjacent('N')
        else: north_case = lab.board[self.x][self.y-1].format_to_adjacent('N')

        if (self.y+1) > lab.max_y: south_case = Case.fake_wall().format_to_adjacent('S')
        else: south_case = lab.board[self.x][self.y+1].format_to_adjacent('S')

        if (self.x+1) > lab.max_x: east_case = Case.fake_wall().format_to_adjacent('E')
        else: east_case = lab.board[self.x+1][self.y].format_to_adjacent('E')

        if (self.x-1) < 0: west_case = Case.fake_wall(self.x-1, self.y).format_to_adjacent('W')
        else: west_case = lab.board[self.x-1][self.y].format_to_adjacent('W')

        return [north_case, south_case, east_case, west_case]