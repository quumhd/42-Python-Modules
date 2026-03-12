
import random
from ex0.Card import Card


class Deck:
    """deck of cards"""
    deck = list()

    def add_card(self, card: Card) -> None:
        """add card to the deck"""
        self.deck.append(card)

    def remove_card(self, card_name: str) -> None:
        """remove card from the deck"""
        to_remove = None
        for card in self.deck:
            if card['name'] == card_name:
                to_remove = card
        if to_remove in self.deck:
            self.deck.remove(to_remove)
        else:
            return "Card is not it Deck"

    def shuffle(self) -> None:
        """shuffle the deck in a random order"""
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        """returns the first card form the deck and removes it"""
        if not self.deck:
            return None
        else:
            return self.deck.pop(0)

    def get_deck_data(self) -> dict:
        """retuns a dict with all deck information"""
        total_cards = 0
        total_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0
        avg_cost = 0
        total_cards = 0
        for card in self.deck:
            if card.type == "creature":
                creatures += 1
            elif card.type == "spell":
                spells += 1
            elif card.type == "artifact":
                artifacts += 1
        for card in self.deck:
            total_cost += card.cost
            total_cards += 1
        avg_cost = round(total_cost / total_cards, 1)
        deck_stats = {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
        return deck_stats
