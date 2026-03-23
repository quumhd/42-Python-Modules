#!/usr/bin/env python3

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """combines 2 spell"""
    def combined_spells(target: str) -> tuple[str, str]:
        return (spell1(target), spell2(target))
    return combined_spells


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """amplifies the power my multiplier"""
    def amplify() -> int:
        return base_spell() * multiplier
    return amplify


def conditional_caster(condition: callable, spell: callable) -> callable:
    """returns a function when if spell is true"""
    def cast_spell() -> str:
        return spell("Dragon")

    def spell_failed() -> str:
        return "Spell fizzled"
    if condition(1) is True:
        return cast_spell
    return spell_failed


def spell_sequence(spells: list[callable]) -> callable:
    """returns a function that casts all spells in order"""
    def cast_spells(target: str) -> list[str]:
        result = list()
        for spell in spells:
            result.append(spell(target))
        return result
    return cast_spells


# helper functions
def fireball(target: str) -> str:
    return f"{target} got hit by fireball"


def heal(target: str) -> str:
    return f"healed {target}"


def damage() -> int:
    return 5


def condition(i: int) -> bool:
    if i == 0:
        return False
    return True


def lightning(target: str) -> str:
    return f"{target} got hit by lightning"


def higher_magic() -> None:
    """demonstrates nested functions"""
    print("=== Higher Magic ===\n")
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined result: {combined('Dragon')}")
    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage, 3)
    print(f"normal: {damage()}, amplified: {amplified()}")
    print("\nTesting contitional caster...")
    result = conditional_caster(condition, fireball)
    print(f"Result: {result()}")
    print("Testing spell sequence...")
    spells = [fireball, heal, lightning]
    sequence = spell_sequence(spells)
    print(f"All spells in order: {sequence('Dragon')}")


if __name__ == "__main__":
    higher_magic()
