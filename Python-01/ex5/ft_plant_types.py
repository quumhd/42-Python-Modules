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
        print(f"{self.height}cm, {self.age} days old")


class Flower(Plant):
    """class Flower inherits from Plant"""
    def __init__(self, name: str, height: int, age: int, colour: str) -> None:
        """initialise parameters"""
        super().__init__(name, height, age)
        self.colour = colour

    def blooming(self) -> None:
        """lets the flower bloom"""
        print(f"{self.name} is blooming")

    def get_colour(self) -> None:
        """prints the colour of the flower"""
        print(f"{self.name} has the colour: {self.colour}")


class Tree(Plant):
    """class Tree inherits from Plant"""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """initialise parameters"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, size: int) -> None:
        """produces shades"""
        print(f"{self.name} produces {size} square meters of shade")

    def get_diamater(self) -> None:
        """prints the diameter of the Tree"""
        print(f"{self.name} has a trunk diameter of {self.trunk_diameter}cm")


class Vegetable(Plant):
    """class Vegetable inherits from Plant"""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """initialise parameters"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self) -> None:
        """prints the vegetable specific info"""
        """get info"""
        print(f"{self.name} is ready to harvest in {self.harvest_season}")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 22, 25, "purple")

    oak = Tree("Oak", 211, 723, 55)
    acorn = Tree("Acorn", 255, 862, 64)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 21, 95, "summer", "vitamin D")

    print(f"{rose.name} ({rose.__class__.__name__}): ", end="")
    rose.get_info()
    rose.blooming()
    print()

    print(f'{oak.name} ({oak.__class__.__name__}):', end="")
    oak.get_info()
    oak.get_diamater()
    print()

    print(f"{tomato.name} ({tomato.__class__.__name__}): ", end="")
    tomato.get_info()
    tomato.print_info()
