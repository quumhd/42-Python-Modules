#!/usr/bin/env python3

from ex2 import BattleStrategy
from ex0.creatures import Creature
from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(creatures: list[tuple[Creature, BattleStrategy]]) -> None:
    print(f"\n\n{creatures}\n\n")
    for i, (creature, strategy) in enumerate(creatures):
        attacker = creature
        attacker_strat = strategy
        for (creature, strategy) in creatures[i:]:
            try:
                attacker.describe()
                print(" vs.")
                creature.describe()
                attacker_strat.act(attacker)
                strategy.act(creature)
            except ValueError as e:
                print("ERROR")
                print(e)
            print()


def main() -> None:
    print("Testing is_valid")
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()
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

    creatures = [(aquabub, normal_strat), (morphagon, aggressive_strat), (aquabub, normal_strat)]
    
    aquabub.describe()
    print("describe")
    
    battle(creatures)

    # print(f"aquabub with normal stat: {normal_strat.is_valid(aquabub)}")
    # print(f"shiftling with normal stat: {normal_strat.is_valid(shiftling)}")
    # print(f"morphagonwith aggressive stat: {aggressive_strat.is_valid(morphagon)}")
    # print(f"shiftling with defensive stat: {defensive_strat.is_valid(shiftling)}")
    # print(f"bloomelle with defensive stat: {defensive_strat.is_valid(blommelle)}")
    # print(f"bloomelle with aggressive stat: {aggressive_strat.is_valid(blommelle)}")
    # print(f"bloomelle with normal stat: {normal_strat.is_valid(blommelle)}")
    # print(f"aquabub with aggressive stat: {aggressive_strat.is_valid(aquabub)}")


if __name__ == "__main__":
    main()
