from models import *

from sys import exit

def init_labyrinthe() -> Labyrinthe:
    lab = Labyrinthe(6, 5)

    lab.place_wall(1, [0, 1, 2, 4, 5])
    lab.place_wall(3, [1, 2, 4])
    lab.place_wall(4, [1, 3])
    lab.place_wall(5, [3, 5])
    lab.place_wall(6, [1])

    lab.place_start(0, 0)
    lab.place_goal(4, 2)

    return lab

def init_player(lab: Labyrinthe) -> Player:
    return Player(lab.start_x, lab.start_y)

def player_move(player: Player, lab: Labyrinthe):
    adjacent_cases = player.adjacent_cases(lab)
    for case in adjacent_cases:
        if case['case'].status == Case.STATUS_GOAL:
            pass # TODO

if __name__ == '__main__':
    lab = init_labyrinthe()
    player = init_player(lab)

    while player.x != lab.goal_x and player.y != lab.goal_y:
        try:
            lab.show(player)
            input('Press Enter to continue...\n')
        except KeyboardInterrupt:
            exit()