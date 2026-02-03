#!/usr/bin/env python3

import sys


def print_inventory(inventory: dict) -> dict:
    """print out a dictionary"""
    for item in inventory["Scarce"]:
        print(f"{item}: {inventory['Scarce'][item]} units")
    for item in inventory["Moderate"]:
        print(f"{item}: {inventory['Moderate'][item]} units")
    for item in inventory["Abundant"]:
        print(f"{item}: {inventory['Abundant'][item]} units")


def parse_arguments() -> dict:
    """turns the input into a dictionary"""
    inventory = {
        "Scarce": {},
        "Moderate":{},
        "Abundant": {}
    }
    to_add = dict()
    quantity = ""
    i = 0
    name = ""
    count = 0
    found = False
    for item in sys.argv[1:]:
        for char in item:
            if char == ':':
                name = item[:i]
                found = True
            if found is True:
                try:
                    count = int(item[i + 1:])
                except (ValueError, TypeError):
                    print("Invalid input")
                    return
                break
            i += 1
        i = 0
        if found is False:
            print("Invalid input")
            return
        found = False
        to_add = {name: count}
        if count <= 3:
            quantity = "Scarce"
        elif count > 3 & count < 10:
            quantity = "Moderate"
        else:
            quantity = "Abundant"
        inventory[quantity].update(to_add)
    return inventory


def print_inventory_analysis(inventory: dict) -> None:
    """prints the inventory analysis"""
    total_items = 0
    for item in inventory["Scarce"]:
        total_items += inventory["Scarce"][item]
    for item in inventory["Moderate"]:
        total_items += inventory["Moderate"][item]
    for item in inventory["Abundant"]:
        total_items += inventory["Abundant"][item]
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")


def print_inventory_statistics(inventory: dict) -> None:
    """prints the most and leasts abundant item"""
    most = None
    most_key = None
    least = None
    least_key = None
    for cat in inventory:
        for item in inventory[cat]:
            if most is None or most < inventory[cat][item]:
                most = inventory[cat][item]
                most_key = item
            if least is None or least > inventory[cat][item]:
                least = inventory[cat][item]
                least_key = item
    print(f"Most abundant: {most_key} (units: {most})")
    print(f"Least abundant: {least_key} (units: {least})")


def print_inventory_categories(inventory: dict) -> None:
    """prints all the items by caegorie"""
    for cat in inventory:
        print(f"{cat}: {inventory[cat]}")


def ft_inventory_system() -> None:
    """to do"""
    inventory = parse_arguments()
    if inventory is None:
        return
    print("=== Inventory System Analysis ===")
    print_inventory_analysis(inventory)
    print("\n=== Current Inventory ===")
    print_inventory(inventory)
    print("\n === Inventory Statistics ===")
    print_inventory_statistics(inventory)
    print("\n=== Item Categories ===")
    print_inventory_categories(inventory)
    print("\n=== Dictionary Properties Demo ===")
    print(inventory.keys())
    print(inventory.values())
    print(inventory['Scarce'].get("sword"))
    


if __name__ == "__main__":
    ft_inventory_system()
