
from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from ex0.CreatureCard import CreatureCard


class EliteCard(Card, Magical, Combatable):
    """Elite card that has abilities from Card, Magical and Combaable"""
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defend: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.init_attack(attack)
        self.init_defend(defend)
        self.init_health(health)
        self.type = "elite_card"

    def play(self, game_state: dict) -> dict:
        """returns the play result"""
        play_result = dict()
        round = 1
        if not game_state:
            round = 1
            mana = 10
        else:
            for rnd in game_state:
                round = rnd + 1
                try:
                    mana = game_state[rnd]['mana']
                except KeyError:
                    pass
        if super().is_playable(mana) is False:
            play_result = {
                'mana': mana,
                'card_played': None,
                'mana_used': 0,
                'effect': "Insufficient mana to play this card"
            }
            return play_result
        play_result = {
            'mana': mana - self.cost,
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to the battlefiled"
            }
        to_add = {round: play_result}
        game_state.update(to_add)
        return play_result

    def attack(self, game_state: dict, target) -> dict:
        """attacks a target with the combat interface"""
        round = 1
        attack_result = dict()
        if isinstance(target, CreatureCard) is False:
            raise ValueError("Target must be a CreatureCard")
        if not game_state:
            round = 1
        else:
            for rnd in game_state:
                round = rnd + 1
        target.health -= self.attack_value
        self.health -= target.attack
        attack_result = {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack_value,
            'combat_resolved': target.health <= 0
        }
        to_add = {round: attack_result}
        game_state.update(to_add)
        return attack_result

    def defend(self, game_state: dict, incoming_damage: int) -> dict:
        """defends an attack with the combat interface"""
        round = 1
        defend_result = dict()
        if not game_state:
            round = 1
        else:
            for rnd in game_state:
                round = rnd + 1
        self.health -= incoming_damage - self.defend_value
        defend_result = {
            'defender': self.name,
            'damage_taken': incoming_damage - self.defend_value,
            'damage_blocked': self.defend_value,
            'still_alive': self.health <= 0
        }
        to_add = {round: defend_result}
        game_state.update(to_add)
        return defend_result

    def get_combat_stats(self) -> dict:
        """returns the combat stats from the combat interface"""
        combat_stats = dict()
        combat_stats = {
            'card_name': self.name,
            'attack': self.attack_value,
            'defend': self.defend_value,
            'health': self.health
        }
        return combat_stats

    def cast_spell(self, game_state: dict, spell_name: str,
                   targets: list) -> dict:
        """casts a spell with the magic interface"""
        play_result = dict()
        target_names = list()
        round = 1
        mana = 100
        if not game_state:
            round = 1
            mana = 10
        else:
            for rnd in game_state:
                round = rnd + 1
                try:
                    mana = game_state[rnd]['mana']
                except KeyError:
                    pass
        for tar in targets:
            target_names.append(tar.name)
        if super().is_playable(mana) is False:
            play_result = {
                'caster': self.name,
                'spell': spell_name,
                'targets': target_names,
            }
            return "Insufficient mana to play this card"
        play_result = {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana used': 4
            }
        to_add = {round: play_result}
        game_state.update(to_add)
        return play_result

    def channel_mana(self, game_state, amount):
        """regenerates mana with the magic interface"""
        play_result = dict()
        round = 1
        if not game_state:
            round = 1
            mana = 10
        else:
            for rnd in game_state:
                round = rnd + 1
                try:
                    mana = game_state[rnd]['mana']
                except KeyError:
                    pass
        play_result = {
            'channeled': amount,
            'total_mana': mana + amount
        }
        to_add = {round: play_result}
        game_state.update(to_add)
        return play_result

    def get_magic_stats(self) -> dict:
        """retuns the magic stats from the magic inerface"""
        magic_stats = dict()
        magic_stats = {
            'channeled_mana': 3
        }
        return magic_stats

    def resolve_effect(self, targets: list) -> dict:
        """applys the spell effect to all targets"""
        for target in targets:
            if isinstance(target, CreatureCard) is False:
                continue
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

    def init_attack(self, attack: int):
        """makes sure attack is positive"""
        if attack >= 0:
            self.attack_value = attack
        else:
            raise ValueError("Attack Value must be 0 or greater")

    def init_defend(self, defend: int):
        """makes sure attack is positive"""
        if defend >= 0:
            self.defend_value = defend
        else:
            raise ValueError("Defend Value must be 0 or greater")

    def init_health(self, health: int):
        """makes sure health is positive"""
        if health > 0:
            self.health = health
        else:
            self.health = 0
