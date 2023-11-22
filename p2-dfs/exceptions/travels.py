class TravelTooFast(Exception):
    def __init__(self) -> None:
        message = "Can't move more than on case at the same time."
        super().__init__(message)

class TravelDiagonaly(Exception):
    def __init__(self) -> None:
        message = "Can't move diagonaly."
        super().__init__(message)