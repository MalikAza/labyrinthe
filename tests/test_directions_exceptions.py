from unittest import TestCase
from main import init_labyrinthe, init_player
from exceptions.directions import *
from models import Case

class DirectionsExceptionsTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.lab = init_labyrinthe()
        self.player = init_player(self.lab)
        self.case = Case()

    def test_case_format_to_adjacent_with_bad_direction(self) -> None:
        self.assertRaises(BadDirection, self.case.format_to_adjacent, self.player, 'NW')

    def test_case_get_coordinates_by_direction_to_player_with_bad_direction(self) -> None:
        self.assertRaises(BadDirection, self.case.get_coordinates_by_direction_to_player, self.player, 'NW')