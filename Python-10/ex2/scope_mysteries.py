#!/usr/bin/env python3

def mage_counter() -> callable:
    """returns a function that counts up each time its called"""
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> callable:
    """returns a functions that adds its power on top of the current power"""
    def add_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    """returns a function that adds the enchantment to the item given"""
    def add_enchantment(item_name: str) -> str:
        nonlocal enchantment_type
        item_name = enchantment_type + " " + item_name
        return item_name
    return add_enchantment


def memory_vault() -> dict[str, callable]:
    """idk"""
    storage = dict()

    def store(key: any, value: any) -> None:
        nonlocal storage
        storage.update({key: value})

    def recall(key: any) -> any:
        nonlocal storage
        if key not in storage:
            return "Memory not found"
        return storage[key]
    return {'store': store, 'recall': recall}


def scope_mysteries() -> None:
    """..."""
    print("=== Memory Dephts ===\n")
    mage_count = mage_counter()
    print("Testing mage counter...")
    print(f"Call 1: {mage_count()}")
    print(f"Call 2: {mage_count()}")
    print(f"Call 3: {mage_count()}")
    print(f"Call 4: {mage_count()}")
    print()
    print("Testing apell accumulator...")
    accumulator = spell_accumulator(100)
    print("Initial Power: 100")
    print(f"Added 50 Power: {accumulator(50)}")
    print(f"Added 25 Power: {accumulator(25)}")
    print(f"Added 100 Power: {accumulator(100)}")
    print()
    print("Testing enchantment factory...")
    sharpness = enchantment_factory("Sharpness V")
    protection = enchantment_factory("Protection IV")
    print(f"Added Sharpness to Sword: {sharpness('Sword')}")
    print(f"Added Protection to Chestplate: {protection('Chestplate')}")
    print()
    print("Testing memory vault...")
    store_recall = memory_vault()
    store = store_recall['store']
    recall = store_recall['recall']
    functions = [mage_counter, spell_accumulator, enchantment_factory]
    store("functions", functions)
    print(f"Added key: functions, value: {functions}")
    print(f"Recall key: functions: {recall('functions')}")
    print(f"Recall with unknown key: {recall('test')}")


if __name__ == "__main__":
    scope_mysteries()
