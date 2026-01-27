#!/usr/bin/env python3

class PlantError(Exception):
    """base fot all plant based exceptions"""
    pass


class NameError(PlantError):
    """error for invalid plant names"""
    pass


class WaterError(PlantError):
    """error for bad water level"""
    pass


class SunError(PlantError):
    """error for bad sunlight hours"""
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """prints the plant health if healthy or raises error if not"""
    is_healthy = True
    try:
        if plant_name is None or plant_name == "":
            raise NameError(f"{plant_name} is not a valid name")
    except NameError as error:
        is_healthy = False
        print(f'Caught NameError: {error}')
    try:
        if water_level > 10:
            raise WaterError(f"Plant has to much water:"
                             f"{water_level}l (max. 10l)")
        elif water_level < 1:
            raise WaterError(f"Plant has not enough Water:"
                             f"{water_level}l (min. 1l)")
    except WaterError as error:
        is_healthy = False
        print(f"Cought WaterError: {error}")
    try:
        if sunlight_hours > 12:
            raise SunError(f"Plants was in the sun for to long:"
                           f"{sunlight_hours}h (max 12h)")
        elif sunlight_hours < 2:
            raise SunError(f"Plant need for sunlight: "
                           f"{sunlight_hours}h (min 1h)")
    except SunError as error:
        is_healthy = False
        print(f"Caught SunError: {error}")
    if is_healthy is True:
        print(f"Plant '{plant_name}' is perfectly healthy")


def test_plant_checks() -> None:
    """tests the erros"""
    print("=== Garaden Plant Health Checker ===\n")
    print("Testing good values:")
    check_plant_health("Tulip", 5, 8)
    print()
    print("Testing empty plant name:")
    check_plant_health(None, 6, 5)
    print()
    print("Testing bad wate level:")
    check_plant_health("Cactus", 66, 4)
    print()
    print("Testing bad sunlight hours:")
    check_plant_health("Tomato", 3, 0)
    print()
    print("All error rasing test complete!")


if __name__ == "__main__":
    test_plant_checks()
