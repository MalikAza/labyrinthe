from models.case import Case
from .coordinates import Coordinates

from typing import TypedDict

class AdjacentCase(TypedDict):
    direction: str
    case: Case
    coordinates: Coordinates