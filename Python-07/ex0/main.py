#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Tests the Abstract Base Class Design"""
    print("=== DataDeck Card Foundation ===\n")
    mana = 10
    card = CreatureCard("Healing Angel", 5, "epic", 1, 11)
    card2 = CreatureCard("Goblin Warrior", 3, "common", 3, 5)
    print("Testing Abstract Base Class Design:\n")
    print(f"CreatureCard Info:\n{card.get_card_info()}\n")
    print(f"Playing {card.name} with {mana} Mana availible")
    print("Playable:", card.is_playable(mana))
    game_state = dict()
    print("Play result:", card.play(game_state, mana))
    print("game_state:", game_state)
    print()
    mana -= card.cost
    mana -= card2.cost
    print("Healing Angel attacks Goblin Warrior")
    print("Attack result:", card.attack_target(card2, game_state))
    print()
    print(f"Testing insufficent mana ({mana} availible)")
    print("Playable:", card.is_playable(mana))
    print()
    print("Abstract pattern succesfully demonstrated")


if __name__ == "__main__":
    main()
