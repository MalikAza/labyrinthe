class Case:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.wall = False
        self.start = False
        self.goal = False

    def show(self, player_x: int = None, player_y: int = None) -> str:
        if self.x == player_x and self.y == player_y: return 'J'

        if self.wall: return 'X'
        if self.start: return 'S'
        if self.goal: return 'G'

        return ' '