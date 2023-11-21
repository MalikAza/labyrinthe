from models.direction import Direction

class BadDirection(Exception):
    "The direction must be one of these: " + ','.join(Direction.VALID)
    pass