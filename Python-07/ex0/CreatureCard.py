
from ex0.Card import Card


class CreatureCard(Card):
    """CreatureCard inherits from Card"""
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.init_attack(attack)
        self.init_health(health)

    def play(self, game_state: dict) -> dict:
        """returns the play result"""
        play_result = dict()
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

    def attack_target(self, target) -> dict:
        """attacks another card"""
        attack_result = dict()
        if isinstance(target, CreatureCard) is False:
            raise ValueError("Target must be a CreatureCard")
        target.health -= self.attack
        attack_result = {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': target.health <= 0
        }
        return attack_result

    def init_attack(self, attack):
        """makes sure attack is positive"""
        if attack >= 0:
            self.attack = attack
        else:
            raise ValueError("Attack Value must be 0 or greater")

    def init_health(self, health):
        """makes sure health is positive"""
        if health > 0:
            self.health = health
        else:
            self.health = 0

    def get_card_info(self) -> dict:
        """retuns a dict with all the card info"""
        card_info = super().get_card_info()
        card_info.update({
            'attack': self.attack,
            'health': self.health
        })
        return card_info
