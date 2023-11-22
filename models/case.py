from __future__ import annotations
from .direction import Direction
from exceptions import BadDirection
class Case:
    STATUS_WALL = 'wall'
    STATUS_START = 'start'
    STATUS_GOAL = 'goal'

    def __init__(self) -> None:
        self.status = None

    def show(self, self_x: int, self_y: int, player: 'Player') -> str:
        if self_x == player.x and self_y == player.y: return 'J'.ljust(2, ' ').rjust(3, ' ')

        match self.status:
            case self.STATUS_WALL:
                return 'X'.ljust(2, ' ').rjust(3, ' ')
            case self.STATUS_START:
                return 'S'.ljust(2, ' ').rjust(3, ' ')
            case self.STATUS_GOAL:
                return 'G'.ljust(2, ' ').rjust(3, ' ')
            case None:
                return ' '.ljust(2, ' ').rjust(3, ' ')
            case _:
                return self.status.ljust(2, ' ').rjust(3, ' ')
            
    def get_coordinates_by_direction_to_player(self, player: 'Player', direction: str) -> 'Coordinates':
        if direction not in Direction.VALID:
            raise BadDirection
        
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
            raise BadDirection
            
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