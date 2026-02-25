
from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """returns test str"""
    return f"Lead transmuted to gold {create_fire()}"


def stone_to_gem() -> str:
    """returns test str"""
    return f"Stone transuted to gem using {create_earth()}"
