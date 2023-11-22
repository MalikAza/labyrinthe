from models import *
from exceptions import BadSortTypeArgument

from sys import exit
from argparse import ArgumentParser

def __get_sort_type() -> str:
    parser = ArgumentParser()
    parser.add_argument('sort_type')
    args = parser.parse_args()
    
    return args.sort_type

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

def resolve_dfs(player: Player, lab: Labyrinthe):
    tries = 0
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            actual_coordinates = player.get_coordinates()
            adjacent_cases = player.adjacent_cases(lab)
            for case in adjacent_cases:
                if case['case'].status == Case.STATUS_GOAL:
                    lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                    player.move_to(case['coordinates'])
                    lab.show(player)
                    print('Finished!')
                    return input('Press Enter to continue...\n')
                if case['direction'] == player.direction:
                    forward_case = case
            
            if forward_case['case'].status != Case.STATUS_WALL and forward_case['coordinates'] not in player.visited:
                player.visited.append(actual_coordinates)
                player.path.append(actual_coordinates)
                tries = 0

                lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                player.move_to(forward_case['coordinates'])
            elif tries != 3:
                    player.change_direction()

                    tries += 1
            else:
                if actual_coordinates not in player.visited:
                    player.visited.append(actual_coordinates)

                lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                player.go_backwards()
                tries = 0
                
        except KeyboardInterrupt:
            exit()

def resolve_bfs(player: Player, lab: Labyrinthe) -> None:
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            exit()
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    sort_type = __get_sort_type()

    lab = init_labyrinthe()
    player = init_player(lab)

    match sort_type:
        case 'dfs':
            resolve_dfs(player, lab)
        case 'bfs':
            resolve_bfs(player, lab)
        case _:
            raise BadSortTypeArgument

    resolve_dfs(player, lab)