#!/usr/bin/env python3

from ex2 import BattleStrategy
from ex0.creatures import Creature
from ex0 import AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(creatures: list[tuple[Creature, BattleStrategy]]) -> None:
    for creature, strategy in creatures:
        print(f"({creature.name}+{strategy.__class__.__name__})", end=" ")
    print("\n")
    for i, (creature, strategy) in enumerate(creatures):
        attacker = creature
        attacker_strat = strategy
        print("* Battle *")
        for (defender, defender_strat) in creatures[i+1:]:
            try:
                print(attacker.describe())
                print(" vs.")
                print(defender.describe())
                print("now fight!")
                attacker_strat.act(attacker)
                defender_strat.act(defender)
            except ValueError as e:
                print("ERROR")
                print(e)
            print()


def main() -> None:
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()
    healing_factory = HealingCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    aquabub = aqua_factory.create_base()
    torragon = aqua_factory.create_evolved()
    shiftling = transform_factory.create_base()
    morphagon = transform_factory.create_evolved()
    sproutling = healing_factory.create_base()
    blommelle = healing_factory.create_evolved()

    print("Tournament 0 (basic)")
    fight1 = [
        (aquabub, normal_strat),
        (morphagon, aggressive_strat),
        ]

    fight2 = [
        (sproutling, normal_strat),
        (torragon, aggressive_strat),
        (shiftling, aggressive_strat)
        ]

    fight3 = [
        (blommelle, defensive_strat),
        (morphagon, aggressive_strat),
        (aquabub, defensive_strat)
        ]

    battle(fight1)
    print("Tournament 1 (multiple)")
    battle(fight2)
    print("Tournament 2 (error)")
    battle(fight3)


if __name__ == "__main__":
    main()
