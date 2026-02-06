#!/usr/bin/env python3

import itertools
from typing import Generator


def random_game_event() -> Generator[dict, None, None]:
    """processes a game event"""
    event_id = 1
    player_set = {"alice", "bob", "charlie", "mike", "leo"}
    level_set = {11, 26, 5, 16, 7, 8, 89, 10, 54, 12, 0, 24, 67, 65}
    event_set = {"killed a monster", "found treasure", "leveled up"}
    player_iter = itertools.cycle(player_set)
    level_iter = itertools.cycle(level_set)
    event_iter = itertools.cycle(event_set)
    while True:
        player = next(player_iter)
        level = next(level_iter)
        event = next(event_iter)
        data = {
            "id": event_id,
            "player": player,
            "level": level,
            "event": event
        }
        event_id += 1
        yield data


def fibonacci_stream() -> Generator[int, None, None]:
    """yields the next fibonacci number"""
    current = 0
    previous = 0
    temp = 0
    while True:
        yield current
        temp = current
        current = previous + current
        previous = temp
        if current == 0:
            current = 1


def prime_number_stream() -> Generator[int, None, None]:
    """yields the next prime number"""
    number = 2
    while True:
        i = 2
        while i <= number:
            if i == number:
                yield number
                break
            if number % i == 0:
                break
            i += 1
        number += 1
        i = 2


def ft_data_stream() -> None:
    """process data, without storing it in memory"""
    print("=== Game Data Stream Processor ===")
    game_event = random_game_event()
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    print("\nProcessing 1000 game events\n")
    for i in range(1000):
        game_data = next(game_event)
        total_events += 1
        if game_data["level"] >= 10:
            high_level_players += 1
        if game_data["event"] == "found treasure":
            treasure_events += 1
        if game_data["event"] == "leveled up":
            level_up_events += 1
        if i < 3:
            print(f"Event {game_data['id']}: {game_data['player']} "
                  f"(level {game_data['level']}) {game_data['event']}")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players: {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci Sequence (first 10): ", end="")
    fib_stream = fibonacci_stream()
    for i in range(10):
        fib_number = next(fib_stream)
        print(fib_number, end="")
        if i < 9:
            print(", ", end="")
        if i == 9:
            print()
    print("Prime numbers (first 5): ", end="")
    prime_stream = prime_number_stream()
    for i in range(5):
        prime_number = next(prime_stream)
        print(prime_number, end="")
        if i < 4:
            print(", ", end="")
        if i == 4:
            print()


if __name__ == "__main__":
    ft_data_stream()
