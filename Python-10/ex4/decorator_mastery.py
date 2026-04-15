#!/usr/bin/env python3

import time
import random
import functools
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def validator(*args, **kwargs) -> str:
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def retry(*args, **kwargs) -> str:
            for i in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i + 1}/{max_attempts})")
                    continue
            return (f"Spell casting failed after {max_attempts} attempts")
        return retry
    return decorator


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for ch in name:
            if ch.isalpha() is False and ch.isspace() is False:
                return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def spell(power: int, spell_name: str):
            return f"Succesfully cast {spell_name} with {power} power"
        return spell(power, spell_name)


def decorator_mastery() -> None:
    # print(test.__name__)
    print("Testing spell_timer...")
    print(f"Result: {cast_fireball()}")
    print()
    print("Testing power_validator...")
    print(return_power(3))
    print(return_power(5))
    print()
    print("Testing retry_spell...")
    print(random_fail())
    print()
    print("Testing MageGuild...")
    mg = MageGuild()
    print(mg.validate_mage_name("Hello World"))
    print(mg.validate_mage_name("Hello World!"))
    print(mg.cast_spell("Lighning", 15))
    print(mg.cast_spell("Lighning", 9))


@spell_timer
def cast_fireball():
    time.sleep(1)
    return "Casted fireball at target"


@power_validator(5)
def return_power(power: int) -> str:
    return f"Power level is {power}"


@retry_spell(5)
def random_fail():
    rand_num = random.randint(1, 5)
    # rand_num = 2
    if rand_num > 2:
        raise Exception
    return "Function sucessfully executed"


if __name__ == "__main__":
    decorator_mastery()
