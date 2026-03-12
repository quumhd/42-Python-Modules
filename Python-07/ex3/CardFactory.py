
from ex0.Card import Card
from abc import ABC, abstractmethod


class CardFactory(ABC):
    """abc for CardFactory"""
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """base class for create_creature"""
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """base class for create_spell"""
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """base class for create_artifact"""
        pass

    def create_themed_deck(self, size: int) -> dict:
        """base class for create_themed_deck"""
        pass

    def get_supported_types(self) -> dict:
        """base class for get_supported_types"""
        pass
