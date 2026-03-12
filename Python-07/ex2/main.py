
from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def get_class_methods(cls):
    return [method for method in dir(cls) if callable(getattr(cls, method))
            and not method.startswith("__")]


def main() -> None:
    """demonstrates the Elite Card"""
    print("=== DataDeck Ability System ===\n")
    print("Elite card capabilities:")
    for parent in EliteCard.__bases__:
        methods = get_class_methods(parent)
        print(f"- {parent.__name__}: {methods}")
    print()
    game_state = dict()
    elite_card = EliteCard("Arcane Warrior", 2, "elite", 7, 3, 15)
    goblin = CreatureCard("Globin", 2, "Common", 4, 5)
    goblin.play(game_state)
    elite_card.play(game_state)
    print("Playing Arcane Warrior (Elite Card)")
    print()
    print("Combat Phase:")
    print(f"Attack result: {elite_card.attack(game_state, goblin)}")
    print(f"Defense result: {elite_card.defend(game_state, 5)}")
    print()
    print("Magic phase:")
    target = [goblin]
    print(f"Spell cast: "
          f"{elite_card.cast_spell(game_state, 'fireball', target)}")
    print(f"Mana channel: {elite_card.channel_mana(game_state, 10)}")
    print()
    print("Multiple interface implementation succesfull!")


if __name__ == "__main__":
    main()
