
from ex0.creatures import Creature
from ex1.capabilities import Sproutling, Bloomelle, Shiftling, Morphagon
from abc import ABC, abstractmethod

from typing import Any


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature) is False:
            raise ValueError("Creature type is not supported by this strategy")
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature) is False:
            raise ValueError(
                "Creature type is not supported by aggressive strategy"
                )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return (
            isinstance(creature, Shiftling) | isinstance(creature, Morphagon)
            )


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature) is False:
            raise ValueError("Creature type is not supported by this strategy")
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return (
            isinstance(creature, Sproutling) | isinstance(creature, Bloomelle)
            )
