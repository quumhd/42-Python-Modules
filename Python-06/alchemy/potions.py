
from .elements import create_fire, create_air, create_earth, create_water


def healing_potion() -> str:
    """healing potion"""
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """strength potion"""
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """invisibility potion"""
    return f"Invisibility potion brewed with {create_air()} and "
    f"{create_water()}"


def wisdom_potion() -> str:
    """wisdom potion"""
    return f"Wisdom potion brewed with all elements: {create_fire()}, "
    f"{create_water()}, {create_air()}, {create_earth()}"
