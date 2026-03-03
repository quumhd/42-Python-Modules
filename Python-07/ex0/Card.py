
from abc import ABC, abstractmethod


class Card(ABC):
    """base class for all cards"""
    def __init__(self, name: str, cost: int, rarity: str):
        """initialisor for the card class"""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        """returns a dict with all the card info"""
        card_info = dict()
        card_info = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }
        return card_info

    def is_playable(self, availible_mana: int) -> bool:
        """checks if player has anought mana to play a card"""
        if self.cost <= availible_mana:
            return True
        return False
