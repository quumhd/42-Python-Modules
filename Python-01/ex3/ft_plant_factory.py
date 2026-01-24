#!/usr/bin/env python3

class Plant:
    """defines the class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialise class parameters"""
        self.name = name
        self.height = height
        self.age = age

    def grow_amount(self, increase: int) -> None:
        """grows the plant by set amount"""
        self.height = self.height + increase

    def age_amount(self, time: int) -> None:
        """ages the plant by set amount"""
        self.age = self.age + time

    def get_info(self) -> None:
        """prints the parameters"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    garden = [
            rose,
            oak,
            cactus,
            sunflower,
            fern
            ]

    created = 0
    print("=== Plant Factory Output ===")
    for plant in garden:
        plant.get_info()
        created += 1
    print()
    print("Total plants created: ", created)
      
