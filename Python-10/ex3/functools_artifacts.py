#!/usr/bin/env python3

import operator
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    """extracts the specified value"""
    valid_operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    if operation not in valid_operations:
        raise ValueError(f"{operation} is not supported")
    operation = valid_operations[operation]
    return reduce(operation, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Spell with power {power} and element {element} casted at {target}"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """returns the partial elements"""
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment,
                                     50, 'lightning')
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """returns nth fibonacci number"""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """returns the default function"""

    @singledispatch
    def exec_spell():
        raise ValueError("Type is not supported")

    @exec_spell.register(int)
    def _(i: int) -> int:
        """function for int"""
        return f"Spell did {i} damage"

    @exec_spell.register(str)
    def _(enchantment: str) -> str:
        """function for str"""
        return f"{enchantment} has been applied"

    @exec_spell.register(list)
    def _(spells: list) -> callable:
        """function for lists"""
        all_spells = ""
        for spell in spells:
            all_spells += exec_spell(spell) + ", "
        return all_spells

    return exec_spell


def functools_artifacts() -> None:
    """demonstrates functools"""
    print("=== Ancient Library ===\n")
    print("Testing spell reducer...")
    data = [1, 5, 6, 3, 7, 8]
    print(f"Data: {data}")
    print(f"Add: {spell_reducer(data, 'add')}")
    print(f"Multiply: {spell_reducer(data, 'multiply')}")
    print(f"Max: {spell_reducer(data, 'max')}")
    print(f"Min: {spell_reducer(data, 'min')}")
    print()
    print("Testing partial enchanter...")
    partial = partial_enchanter(base_enchantment)
    print(partial['fire_enchant']("goblin"))
    print()
    print("Testing memoized fibonacci...")
    print(f"10th fibonacci number: {memoized_fibonacci(10)}")
    print(memoized_fibonacci.cache_info())
    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(5))
    print(dispatcher("Sharpness"))
    print(dispatcher([5, "Protection", 6]))


if __name__ == "__main__":
    functools_artifacts()
