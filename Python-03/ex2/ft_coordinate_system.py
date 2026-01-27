#!/usr/bin/env python3

import math
import sys


def calc_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    """calculates the distance between two 3D Points"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def parse_coordinates(input: tuple[str, str, str]) -> tuple[int, int, int]:
    """convert the string input to ints"""
    x, y, z = input
    x = int(x)
    y = int(y)
    z = int(z)
    return x, y, z


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    test_coords = 23, 35, 76
    zero_coords = 0, 0, 0
    preview = calc_distance(test_coords, zero_coords)
    print(f"Position created at {test_coords}")
    print(f"Distance between {zero_coords} and {test_coords}: {preview:.2f}m")
    print()
    try:
        p1 = sys.argv[1].split(",")
    except IndexError:
        print("No arguments given using standart values.")
        p1 = "0", "0", "0"
    try:
        p2 = sys.argv[2].split(",")
    except IndexError:
        print("No second argument given, using standart values\n")
        p2 = "0", "0", "0"
    try:
        bad_args = "test", "abc", "banana"
        print(f"Parsing invalid coordinate: {bad_args}")
        parse_coordinates(bad_args)
    except ValueError as error:
        print(f"{type(error).__name__}: {error}\n")
    try:
        p1 = parse_coordinates(p1)
    except ValueError as error:
        print(f"ValueError: {error}")
    try:
        p2 = parse_coordinates(p2)
    except ValueError as error:
        print(f"ValueError: {error}")
    distance = calc_distance(p1, p2)
    print(f"Player 1 is at: {p1}")
    print(f"Player 2 is at: {p2}")
    print(f"Distance between the players: {distance:.2f}m")


if __name__ == "__main__":
    ft_coordinate_system()
