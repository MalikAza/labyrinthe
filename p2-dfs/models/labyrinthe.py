from .case import Case
from custom_types import CaseToShow

from typing import List

class Labyrinthe:
    BASE_COLUMN_INDEX = 0
    BASE_ROW_INDEX = 0
    
    def __init__(self, max_index_x, max_index_y) -> None:
        self.max_index_x = max_index_x
        self.max_index_y = max_index_y
        self.board = [[Case() for y in range(max_index_y+1)] for x in range(max_index_x+1)]

    def place_wall(self, column_index: int, indexes: List[int]) -> None:
        for index, case in enumerate(self.board[column_index]):
            if index in indexes:
                case.status = Case.STATUS_WALL

    def place_start(self, x: int, y: int) -> None:
        self.start_x = x
        self.start_y = y
        self.board[x][y].status = Case.STATUS_START

    def place_goal(self, x: int, y: int) -> None:
        self.goal_x = x
        self.goal_y = y
        self.board[x][y].status = Case.STATUS_GOAL

    def show(self, player) -> None:
        for y in range(self.max_index_y+1):
            cases: List[CaseToShow] = []
            for x, column in enumerate(self.board):
                cases.append(column[y].format_to_show(x, y))

            message = '|'
            message += '|'.join([case['case'].show(case['x'], case['y'], player.x, player.y)
                                    for case in cases])
            message += '|'

            print(message)

        print(f"\nPlayer steps: [{player.steps}]")