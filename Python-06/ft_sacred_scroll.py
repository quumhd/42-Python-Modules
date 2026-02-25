#!/usr/bin/env python3


import alchemy


def ft_sacred_scroll() -> None:
    """  """
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())
    print()
    print("Testing package-level access (controlled by __inti__.py)")
    print("alchemy.create_fire():", alchemy.create_fire())
    print("alchemy.create_water():", alchemy.create_water())
    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): Attribute Error - not exposed")
    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_earth(): Attribute Error - not exposed")
    print()
    print("Package metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    ft_sacred_scroll()
