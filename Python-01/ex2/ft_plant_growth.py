#!/usr/bin/env python3

class Plant:
    """defines the class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initalise class parameters"""
        self.name = name
        self.height = height
        self.age = age

    def grow

    def get_info(self) -> None:
        """prints the parameters"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
