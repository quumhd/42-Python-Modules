#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """sorts the list in descending order and returns it"""
    sorted_list = sorted(artifacts, key=lambda pwr: -pwr['power'])
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """returns a list of mages that have a greater power than min_power"""
    filtered_list = list(filter(lambda pwr: pwr['power'] >= min_power, mages))
    return filtered_list


def spell_tranformer(spells: list[str]) -> list[str]:
    """adds '* ' infront and ' *' after every mages name"""
    prefix = "* "
    suffix = " *"
    maped_list = list(map(lambda a: prefix + a + suffix, spells))
    return maped_list


def mage_stats(mages: list[dict]) -> dict:
    """returns a dict with max_power, min_power, avg_power"""
    max_power = max(map(lambda a: a['power'], mages))
    min_power = min(map(lambda a: a['power'], mages))
    avg_power = sum(map(lambda a: a['power'], mages)) / len(mages)
    stats = {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }
    return stats


def lamdba_spells() -> None:
    """demonstrates the lamda functions"""
    print("=== Lambda Spells ===\n")
    artifacts = [
        {'name': 'Water Chalice', 'power': 94, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 65, 'type': 'armor'},
        {'name': 'Wind Cloak', 'power': 87, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 96, 'type': 'relic'}
        ]
    mages = [
        {'name': 'Phoenix', 'power': 98, 'element': 'lightning'},
        {'name': 'Zara', 'power': 90, 'element': 'lightning'},
        {'name': 'Zara', 'power': 79, 'element': 'shadow'},
        {'name': 'Sage', 'power': 95, 'element': 'wind'},
        {'name': 'Casey', 'power': 55, 'element': 'ice'}
        ]
    spells = ['darkness', 'shield', 'lightning', 'earthquake']

    print("testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\ntesting power filter...")
    print(power_filter(mages, 90))
    print("\ntesting spell_transformer...")
    print(spell_tranformer(spells))
    print("\ntesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    lamdba_spells()
