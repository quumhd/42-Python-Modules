
from abc import ABC, abstractmethod


class Combatable(ABC):
    """abc for combat interface"""
    @abstractmethod
    def attack(self, game_state: dict, target) -> dict:
        pass

    @abstractmethod
    def defend(self, game_state: dict, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
