
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self):
        self.name = "Creature"
        self.creature_type = "Creature"

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self):
        self.name = "Flameling"
        self.creature_type = "Fire"

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        self.name = "Pyrodon"
        self.creature_type = "Fire/Flying"

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        self.name = "Aquabub"
        self.creature_type = "Water"

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self):
        self.name = "Torragon"
        self.creature_type = "Water"

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
