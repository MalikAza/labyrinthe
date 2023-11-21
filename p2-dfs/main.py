from models.labyrinthe import Labyrinthe
from models.player import Player

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
    lab = init_labyrinthe()
    player = init_player(lab)

    lab.show(player.x, player.y)