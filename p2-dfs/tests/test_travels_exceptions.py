from unittest import TestCase
from main import init_labyrinthe, init_player
from exceptions.travels import *

class TravelsExceptionsTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.lab = init_labyrinthe()
        self.player = init_player(self.lab)

    def test_cant_move_more_than_one_case(self) -> None:
        coordinates_south = {
            'x': self.player.x,
            'y': self.player.y+2
        }
        coordinates_north = {
            'x': self.player.x,
            'y': self.player.y-2
        }
        coordinates_east = {
            'x': self.player.x+2,
            'y': self.player.y
        }
        coordinates_west = {
            'x': self.player.x-2,
            'y': self.player.y
        }

        self.assertRaises(TravelTooFast, self.player.move_to, coordinates_south)
        self.assertRaises(TravelTooFast, self.player.move_to, coordinates_north)
        self.assertRaises(TravelTooFast, self.player.move_to, coordinates_east)
        self.assertRaises(TravelTooFast, self.player.move_to, coordinates_west)

    def test_cant_move_diagonaly(self) -> None:
        coordinates_top_left = {
            'x': self.player.x-1,
            'y': self.player.y+1
        }
        coordinates_top_right = {
            'x': self.player.x+1,
            'y': self.player.y+1
        }
        coordinates_bottom_left = {
            'x': self.player.x-1,
            'y': self.player.y-1
        }
        coordinates_bottom_right = {
            'x': self.player.x+1,
            'y': self.player.y-1
        }

        self.assertRaises(TravelDiagonaly, self.player.move_to, coordinates_top_left)
        self.assertRaises(TravelDiagonaly, self.player.move_to, coordinates_top_right)
        self.assertRaises(TravelDiagonaly, self.player.move_to, coordinates_bottom_left)
        self.assertRaises(TravelDiagonaly, self.player.move_to, coordinates_bottom_right)