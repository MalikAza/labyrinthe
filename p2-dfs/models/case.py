from __future__ import annotations
from .direction import Direction
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
            
    def get_coordinates_by_direction_to_player(self, player: 'Player', direction: str) -> 'Coordinates':
        if direction not in Direction.VALID:
            raise 'BadDirection'
        
        match direction:
            case Direction.NORTH:
                return {'x': player.x, 'y': player.y-1}
            case Direction.SOUTH:
                return {'x': player.x, 'y': player.y+1}
            case Direction.WEST:
                return {'x': player.x-1, 'y': player.y}
            case Direction.EAST:
                return {'x': player.x+1, 'y': player.y}
    
    def format_to_adjacent(self, player: 'Player', direction: str) -> 'AdjacentCase':
        if direction not in Direction.VALID:
            raise 'BadDirection'
            
        return {
            'direction': direction,
            'case': self,
            'coordinates': self.get_coordinates_by_direction_to_player(player, direction)
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