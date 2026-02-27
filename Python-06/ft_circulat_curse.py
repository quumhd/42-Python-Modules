#!/usr/bin/env python3

from alchemy.grimoire import record_spell, validate_ingredients


def ft_circulat_curse() -> None:
    """wda"""
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredients(\"fire air\"):", validate_ingredients("fire air"))
    print("Testing ingredients(\"dragon scales\"):", validate_ingredients("dragon scales"))
    print()
    print("Testing spell recording with validation")
    print("record_spell(\"Fireball\"), (\"fire air\"):", record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\"), (\"shadow\"):", record_spell("Dark Magic", "shadow"))
    print()
    from alchemy.grimoire import record_spell as late_record_spell
    print("Testing late import technique")
    print("late_record_spell(\"Lightning\"), (\"air\"):", late_record_spell("Lightning", "air"))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circulat_curse()
