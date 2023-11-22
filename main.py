from models import Labyrinthe, Player
from exceptions import BadSortTypeArgument
import part_two_dfs
import part_three_bfs

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

if __name__ == '__main__':
    sort_type = __get_sort_type()

    lab = init_labyrinthe()
    player = init_player(lab)

    match sort_type:
        case 'dfs':
            part_two_dfs.resolve(player, lab)
        case 'bfs':
            part_three_bfs.resolve(player, lab)
        case _:
            raise BadSortTypeArgument