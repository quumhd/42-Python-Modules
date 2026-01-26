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
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(7):
        rose.grow_amount(2)
        rose.age_amount(1)
    print("=== Day 7 ===")
    rose.get_info()
