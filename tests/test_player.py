from main import init_labyrinthe, init_player
from models import Direction

from unittest import TestCase

class PlayerTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.lab = init_labyrinthe()
        self.player = init_player(self.lab)

    def test_adjacent_cases_is_sorted(self):
        adjacent_cases = self.player.adjacent_cases(self.lab)

        self.assertAlmostEqual(adjacent_cases[0]['direction'], Direction.SOUTH)
        self.assertAlmostEqual(adjacent_cases[1]['direction'], Direction.EAST)
        self.assertAlmostEqual(adjacent_cases[2]['direction'], Direction.NORTH)
        self.assertAlmostEqual(adjacent_cases[3]['direction'], Direction.WEST)