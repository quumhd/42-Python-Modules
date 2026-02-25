
from .validator import valid_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """creates a new spell"""
    if valid_ingredients(ingredients) == "VALID":
        print("valid")
