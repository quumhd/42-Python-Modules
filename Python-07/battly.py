#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def use_factory(creature_factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base_creature = creature_factory.create_base()
        evolved_creature = creature_factory.create_evolved()
    except Exception:
        raise Exception("Cannot create base and evolved creatures")
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    base_creature_1 = factory_1.create_base()
    base_creature_2 = factory_2.create_base()
    print(base_creature_1.describe())
    print(" vs.")
    print(base_creature_2.describe())
    print(" fight!")
    print(base_creature_1.attack())
    print(base_creature_2.attack())


def main():
    use_factory(FlameFactory())
    print()
    use_factory(AquaFactory())
    print()
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
