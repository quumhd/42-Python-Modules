#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """waters the plants, while always ensuring cleanup"""
    print("Opening watering systems")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant name")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """tets the water_plants function"""
    print("Testing watering with valid plants:")
    valid_plants = ["tulip", "cactus", "tomato", "lettuce", "carrots"]
    water_plants(valid_plants)
    print()
    print("Testing watering system with invalid plants:")
    invalid_plants = ["tulip", "cactus", None, "lettuce", "carrots"]
    water_plants(invalid_plants)
    print()
    print("Cleanup always happend, even when an error occured")


if __name__ == "__main__":
    print("=== Garden Watering Systems ===")
    test_watering_system()
