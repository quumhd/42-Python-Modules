
from ex0.Card import Card, CreatureCard


class SpellCard(Card):
    """SpellCard inherits from Card"""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.played = False
        self.type = "spell"

    def play(self, game_state: dict, mana) -> dict:
        """retuns the play result"""
        play_result = dict()
        round = 1
        if not game_state:
            round = 1
        else:
            for rnd in game_state:
                round = rnd + 1
        if self.played is True:
            play_result = {
                'mana': mana,
                'card_played': None,
                'mana_used': 0,
                'effect': "You already used this spell"
            }
            return play_result
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
            'effect': "Creature summoned to the battlefiled"
            }
        to_add = {round: play_result}
        game_state.update(to_add)
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
            elif self.effect_type == "debuff":
                target.attack -= 1
            else:
                return
