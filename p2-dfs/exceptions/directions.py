from models.case import Case

class BadDirection(Exception):
    "The direction must be one of these: " + ','.join(Case.VALID_DIRECTIONS)
    pass