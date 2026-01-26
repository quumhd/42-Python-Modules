#!/usr/bin/env python3

def garden_operations(error_type:  str) -> None:
    """executes the tests where the errors appear"""
    if error_type == "ValueError":
        int("abc")
    elif error_type == "ZeroDivisionError":
        10 / 0
    elif error_type == "FileNotFoundError":
        open("missing.txt")
    elif error_type == "KeyError":
        dict = {"tulip": 5}
        dict["error"]


def test_error_types() -> None:
    """handels the errors"""
    cought_error = False
    print("=== Testing error types ===")
    print()
    print("Testing ValueError:")
    try:
        garden_operations("ValueError")
    except ValueError as error:
        print(f"Caught ValueError {error}")
        cought_error = True
    print()
    print("Testing ZeroDivisionError:")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as error:
        print(f"Cought ZeroDivisionError: {error}")
        cought_error = True
    print()
    print("Testing FilesNotFoundError:")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
        cought_error = True
    print()
    print("Testing KeyError:")
    try:
        garden_operations("KeyError")
    except KeyError as error:
        print(f"Cought KeyError: {error}")
        cought_error = True
    print()
    print("Testing multiple errors:")
    try:
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
    except (ValueError, ZeroDivisionError):
        print("Caught multiple errors")
        cought_error = True
    print()
    if cought_error is True:
        print("Caught an error, but program continued")
    print("All error types succesfully tested!")


if __name__ == "__main__":
    test_error_types()
