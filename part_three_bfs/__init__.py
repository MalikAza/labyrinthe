from models import Player, Labyrinthe, Case
from custom_types import Coordinates

from sys import exit
from copy import copy
from typing import List

def resolve(player: Player, lab: Labyrinthe):
    player.can_travel_fast = True
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            actual_coordinates = player.get_coordinates()
            if actual_coordinates not in player.visited:
                player.visited.append(actual_coordinates)

            # register possible coords
            for case in player.adjacent_cases(lab):
                if case['case'].status != Case.STATUS_WALL and case['coordinates'] not in player.visited and case['coordinates'] not in player.path:
                    player.path.append(case['coordinates'])
                if case['case'].status == Case.STATUS_GOAL:
                    player.path[-1] = case['coordinates']
                    player.visited.append(case['coordinates'])
                    break

            # move to next possible coords
            lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
            player.move_to(player.path.pop(0))
                
        except KeyboardInterrupt:
            exit()

    # retrieve best branch
    fast_path : List[Coordinates] = []
    fast_path.append(player.visited.pop(-2))
    for coord in player.visited[::-1]:
        if coord in [adjacent['coordinates'] for adjacent in player.adjacent_cases(lab)]:
            fast_path.append(coord)
            player.move_to(coord)

    lab.show(player)
    print('Finished!')
    print('Path: ' + ', '.join([f"({coord['x']}, {coord['y']})" for coord in fast_path[::-1]]))
    print(f"Path length: {len(fast_path)}\n")
    input('Press Enter to continue...\n')