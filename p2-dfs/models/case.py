from __future__ import annotations

class Case:
    STATUS_WALL = 'wall'
    STATUS_START = 'start'
    STATUS_GOAL = 'goal'

    def __init__(self) -> None:
        self.status = None

    def show(self, self_x: int, self_y: int, player_x: int, player_y: int) -> str:
        if self_x == player_x and self_y == player_y: return 'J'

        match self.status:
            case self.STATUS_WALL:
                return 'X'
            case self.STATUS_START:
                return 'S'
            case self.STATUS_GOAL:
                return 'G'
            case _:
                return ' '
            
    def format_to_adjacent(self, direction: str) -> 'AdjacentCase':
        return {
            'direction': direction,
            'case': self
        }
    
    def format_to_show(self, x: int, y: int) -> 'CaseToShow':
        return {
            'x': x,
            'y': y,
            'case': self
        }

    @staticmethod
    def fake_wall() -> Case:
        case = Case()
        case.status = Case.STATUS_WALL

        return case