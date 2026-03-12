
from abc import ABC, abstractmethod


class GameStrategie(ABC):
    """abc for Game stratagies"""
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """base function for execute turn"""
        pass

    def get_strategy_name(self) -> str:
        """base function for get_stategy_name"""
        pass

    def prioritize_targets(self, availible_targets: list) -> list:
        """base function for proritize_targets"""
        pass
