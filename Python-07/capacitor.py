#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def use_healing_factory(creature_factory: HealingCreatureFactory) -> None:
    try:
        base_creature = creature_factory.create_base()
        evolved_creature = creature_factory.create_evolved()
    except Exception:
        raise Exception("Cannot create base and evolved creatures")
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())


def use_transform_factory(creature_factory: TransformCreatureFactory) -> None:
    try:
        base_creature = creature_factory.create_base()
        evolved_creature = creature_factory.create_evolved()
    except Exception:
        raise Exception("Cannot create base and evolved creatures")
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def main():
    print("Testing Creature with healing capibiliy:")
    use_healing_factory(HealingCreatureFactory())
    print()
    print("Testing Creature with transform capibiliy")
    use_transform_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
