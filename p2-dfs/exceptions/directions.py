from models.direction import Direction

class BadDirection(Exception):
    def __init__(self) -> None:
        message = "The direction must be one of these: " + ','.join(Direction.VALID)
        super().__init__(message)