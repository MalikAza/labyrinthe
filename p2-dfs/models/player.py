from .case import Case
from custom_types import AdjacentCase

from typing import List

class Player:
    def __init__(self, start_x: int, start_y: int) -> None:
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.direction = 'S'

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

    def adjacent_cases(self, lab) -> List[AdjacentCase]:
        def fake_wall(x: int, y: int) -> Case:
            wall_case = Case(x, y)
            wall_case.wall = True

            return wall_case
        
        def format_case(case: Case, direction: str) -> AdjacentCase:
            return {
                'direction': direction,
                'case': case
            }

        if (self.y-1) < 0: north_case = fake_wall(self.x, self.y-1)
        else: north_case = lab.board[self.x][self.y-1]
        north_case = format_case(north_case, 'N')

        if (self.y+1) > lab.max_y: south_case = fake_wall(self.x, self.y+1)
        else: south_case = lab.board[self.x][self.y+1]
        south_case = format_case(south_case, 'S')

        if (self.x+1) > lab.max_x: east_case = fake_wall(self.x+1, self.y)
        else: east_case = lab.board[self.x+1][self.y]
        east_case = format_case(east_case, 'E')

        if (self.x-1) < 0: west_case = fake_wall(self.x-1, self.y)
        else: west_case = lab.board[self.x-1][self.y]
        west_case = format_case(west_case, 'W')

        return [north_case, south_case, east_case, west_case]