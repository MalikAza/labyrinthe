from models.case import Case

from typing import TypedDict

class AdjacentCase(TypedDict):
    direction: str
    case: Case