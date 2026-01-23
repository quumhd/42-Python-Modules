#!/usr/bin/env python3

class Plant:
    """defines the class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initalise class parameters"""
        self.name = name
        self.height = height
        self.age = age

    def print_plant_information(self) -> None:
        """prints the parameters"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Welcome to My Garden ===")
    rose.print_plant_information()
    sunflower.print_plant_information()
    cactus.print_plant_information()
    print("=== End of Program ===")
