

def validate_ingredients(ingredients: str) -> str:
    """vaidates ingedients"""
    ingredient = ingredients.split()
    for i in ingredient:
        if i == "fire" or i == "water" or i == "earth" or i == "air":
            pass
        else:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
