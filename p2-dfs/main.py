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

def resolve(player: Player, lab: Labyrinthe):
    tries = 0
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            for case in player.adjacent_cases(lab):
                if case['case'].status == Case.STATUS_GOAL:
                    return player.move_to_direction(case['direction'])
                if case['direction'] == player.direction:
                    player_direction_case = case
            
            if player_direction_case['case'].status != Case.STATUS_WALL and player.get_coordinates_from_direction(player.direction) not in player.stack:
                tries = 0
                player.move_to_direction(player.direction)
            else:
                if tries >= 3:
                    new_path = False
                    while new_path != True:
                        player.go_backwards()
                        for case in player.adjacent_cases(lab):
                            if case['case'].status != Case.STATUS_WALL and player.get_coordinates_from_direction(player.direction) not in player.stack:
                                player.direction = case['direction']
                                new_path = True
                else:
                    player.change_direction()
                    tries += 1
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    lab = init_labyrinthe()
    player = init_player(lab)

    resolve(player, lab)