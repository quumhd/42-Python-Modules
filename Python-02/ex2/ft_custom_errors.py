#!/usr/bin/env python3

class GardenError(Exception):
    """base class for all garden realted errors"""
    pass


class PlantError(GardenError):
    """for all plant related errors"""
    pass


class WaterError(GardenError):
    """for all watering related errors"""
    pass


def check_plant_age(age: int) -> None:
    """raises a PlantError if the age is negative"""
    if age < 0:
        raise PlantError(f"Plants cannot have a negative age: {age}")
    elif age > 100:
        raise PlantError(f"the plant is wilting at age: {age}")


def check_water_level(water_level: int) -> None:
    """raises a WaterError if the water level is bad for the plant"""
    if water_level < 10:
        raise WaterError(f"The plant at least 10 liters, has {water_level}")


def raise_custom_error() -> None:
    """tests all the errors and outputs them"""
    print("Testing custom PlantError:")
    try:
        check_plant_age(-2)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing custom PlantError:")
    try:
        check_plant_age(111)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing custom WaterError:")
    try:
        check_water_level(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing custom GardenError:")
    try:
        check_water_level(-5)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()
    print("Testing custom GardenError:")
    try:
        check_plant_age(-5)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()
    print("Testing custom GardenError:")
    try:
        check_plant_age(111)
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    raise_custom_error()
