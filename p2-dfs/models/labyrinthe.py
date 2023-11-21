from .case import Case

from typing import List

class Labyrinthe:
    def __init__(self, given_x, given_y) -> None:
        self.max_x = given_x
        self.max_y = given_y
        self.board = [[Case(x, y) for y in range(given_y+1)] for x in range(given_x+1)]

    def place_wall(self, column_index: int, indexes: List[int]) -> None:
        for index, box in enumerate(self.board[column_index]):
            if index in indexes:
                box.wall = True

    def place_start(self, x: int, y: int) -> None:
        self.start_x = x
        self.start_y = y
        self.board[x][y].start = True

    def place_goal(self, x: int, y: int) -> None:
        self.goal_x = x
        self.goal_y = y
        self.board[x][y].goal = True

    def show(self, player) -> None:
        for i in range(self.max_y+1):
            cases = []
            for column in self.board:
                cases.append(column[i])
            print('|' + '|'.join([case.show(player.x, player.y) for case in cases]) + '|\n')

        print(f"Player steps: [{player.steps}]")