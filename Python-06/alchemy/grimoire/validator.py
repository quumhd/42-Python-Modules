

def validate_ingredients(ingredients: str) -> str:
    """vaidates ingedients"""
    if ingredients == "fire":
        return "VALID"
    elif ingredients == "water":
        return "VALID"
    elif ingredients == "earth":
        return "VALID"
    elif ingredients == "air":
        return "VALID"
    else:
        return "INVALID"
