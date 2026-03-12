
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    """shows off the deck builder system"""
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    game_state = dict()
    creature = CreatureCard("Goblin", 3, "common", 2, 10)
    spell = SpellCard("Zap", 2, "common", "damage")
    artifact = ArtifactCard("Damage Buff", 2, "rage", 2, "+1 damage")
    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)
    print(f"Deck Stats: {deck.get_deck_data()}")
    print()
    print("Drawing and playing cards:\n")
    draw1 = deck.draw_card()
    print(f"Drew: {draw1.name} ({draw1.type})")
    print(f"Play result: {draw1.play(game_state)}")
    print()
    draw2 = deck.draw_card()
    print(f"Drew: {draw2.name} ({draw2.type})")
    print(f"Play result: {draw2.play(game_state)}")
    print()
    draw3 = deck.draw_card()
    print(f"Drew: {draw3.name} ({draw3.type})")
    print(f"Play result: {draw3.play(game_state)}")
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
