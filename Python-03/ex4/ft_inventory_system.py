#!/usr/bin/env python3

import sys


def print_inventory(inventory: dict[str, int]) -> dict[str, int]:
    """print out a dictionary"""
    for item in inventory:
        print(f"{item}: {inventory[item]}")


def parse_arguments() -> dict[str, int]:
    """turns the input into a dictionary"""
    inventory = dict()
    to_add = dict()
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
                count = int(item[i + 1:])
                break
            i += 1
        i = 0
        if found is False:
            print("Invalid input")
            return
        else:
            found = False
        to_add = {name: count}
        inventory.update(to_add)
    return inventory


def ft_inventory_system() -> None:
    """to do"""
    inventory = parse_arguments()
    print("=== Inventory System Analysis ===")
    print_inventory(inventory)


if __name__ == "__main__":
    ft_inventory_system()
