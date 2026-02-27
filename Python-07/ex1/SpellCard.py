
from ex0.Card import Card, CreatureCard


class SpellCard(Card):
    """SpellCard inherits from Card"""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.played = False

    def play(self, game_state: dict) -> dict:
        """retuns the play result"""
        play_result = dict()
        if self.played is True:
            play_result = {
                'spell_played': "You already used this spell"
            }
            return play_result
        if super().is_playable(game_state['mana']) is False:
            play_result = {
                'mana': "insuffient mana to play this card"
            }
            return play_result
        play_result = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to the battlefiled"
            }
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        """applys the spell effect to all targets"""
        for target in targets:
            if isinstance(target, CreatureCard):

                return
            if self.effect_type == "damage":
                target.health -= 2
            elif self.effect_type == "heal":
                target.health += 2
            elif self.effect_type == "buff":
                target.attack += 1
            else:
                return

