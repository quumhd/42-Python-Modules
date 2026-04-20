
from ex0.creatures import Creature
from abc import ABC, abstractmethod


class HealCapibility(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapibility(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapibility):
    def __init__(self) -> None:
        self.name = "Sproutling"
        self.creature_type = "Grass"

    def attack(self) -> str:
        return f"{self.name} is using Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapibility):
    def __init__(self) -> None:
        self.name = "Bloomelle"
        self.creature_type = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def describe(self):
        return super().describe()


class Shiftling(Creature, TransformCapibility):
    def __init__(self) -> None:
        self.name = "Shiftling"
        self.creature_type = "Normal"
        self.transformed = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normaly."
        return f"{self.name} performs a boosted strike"

    def transform(self):
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} return to normal"

    def describe(self):
        return super().describe()


class Morphagon(Creature, TransformCapibility):
    def __init__(self) -> None:
        self.name = "Morphagon"
        self.creature_type = "Normal/Dragon"
        self.transformed = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normaly."
        return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form"

    def describe(self):
        return super().describe()
