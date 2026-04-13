#!/usr/bin/env python3

import functools
import time


class MageGuild():
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def timer(*args, **kwargs):
        start_time = time.perf_counter()
        elapsed = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return func(*args, **kwargs)
    return timer


def power_validator(min_power: int) -> callable:
    pass


def retry_spell(max_attempts: int) -> callable:
    pass


def decorator_mastery() -> None:
    print("Testing pell timer...")
    print("adding every number until 10000")
    print(f"Result: {test()}")


@spell_timer
def test():
    total = 0
    for i in range(10000):
        total += i
    return total


if __name__ == "__main__":
    decorator_mastery()
