
from ex0.Card import Card


class ArtifactCard(Card):
    """ArtifactCard inherits from card"""
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.activated = 0
        self.type = "artifact"

    def play(self, game_state: dict) -> dict:
        """"""
        play_result = dict()
        round = 1
        if not game_state:
            round = 1
            mana = 10
        else:
            for rnd in game_state:
                round = rnd + 1
            mana = game_state[rnd]['mana']
        if self.activated == 0:
            self.activated = round - 1
        if super().is_playable(mana) is False:
            play_result = {
                'mana': mana,
                'card_played': None,
                'mana_used': 0,
                'effect': "Insufficient mana to play this card"
            }
            return "Insufficient mana to play this card"
        play_result = {
            'mana': mana - self.cost,
            'card_played': self.name,
            'mana_used': self.cost,
            }
        if round - self.activated >= 0:
            play_result.update(self.activate_ability())
        else:
            play_result.update({'effect': "effect run out"})
        to_add = {round: play_result}
        game_state.update(to_add)
        return play_result

    def activate_ability(self) -> dict:
        """activate ability"""
        ability = {
            'effect': self.effect
            }
        return ability
