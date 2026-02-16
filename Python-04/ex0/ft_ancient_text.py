#!/usr/bin/env python3


import sys


def ft_ancient_text() -> None:
    """reads out a file"""
    try:
        print(f"Trying to access {sys.argv[1]}\n")
        with open(sys.argv[1], "r") as f:
            print("Connection successfully established\n")
            for line in f:
                print(line, end="")
            print()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IndexError:
        print("Specify a sotrage unit")
    finally:
        print("\nStorage unit closed")


if __name__ == "__main__":
    ft_ancient_text()
