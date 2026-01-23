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
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    tomato = Plant("Rose", 25, 30)
    Plant.print_plant_information(tomato)
    print("=== End of Program ===")
