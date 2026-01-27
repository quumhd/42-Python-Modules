#!/usr/bin/env python3

import sys


def print_arguments() -> None:
    """prints the arguments given in the command line"""
    print("=== Command Quest ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print_arguments()
