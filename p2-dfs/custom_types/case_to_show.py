from models.case import Case

from typing import TypedDict

class CaseToShow(TypedDict):
    x: int
    y: int
    case: Case