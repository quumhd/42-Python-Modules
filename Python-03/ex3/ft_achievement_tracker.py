#!/usr/bin/env python3

class Player:
    """class Player, with name and achievements"""
    def __init__(self, name: str, achievements: list[str]) -> None:
        """initialise name and achievements"""
        self.name = name
        self.achievements = achievements

    def print_achievements(self) -> None:
        """prints all the achievements of the player"""
        print(f"Player {self.name}'s achievements: {self.achievements}")

    def get_achievements(self) -> set[str]:
        """returns the achievements of the player"""
        return self.achievements


def print_all_achievements(*args: set[str]) -> None:
    """prints out all unique achievements the players have"""
    all_achievements = set()
    for s in args:
        all_achievements = all_achievements | s
    print(f"All achievements: {all_achievements}\n")
    print(f"Number of achievements: {len(all_achievements)}\n")


def print_common_achievements(*args: set[str]) -> None:
    """prints all achievements that all player have in common"""
    common_achievements = args[0]
    for s in args:
        common_achievements = common_achievements & s
    print(f"Common to all players: {common_achievements}\n")


def print_rare_achievements(*args: set[str]) -> None:
    """prints all achievements that only one player gathered"""
    temp = set()
    in_last = set()
    in_both = set()
    rare_achievements = set()
    for s in args:
        for j in args:
            temp = s - j
            if len(temp) != 0:
                if len(in_both) == 0:
                    in_both = temp
                in_both = temp & in_last & in_both
                in_last = temp
        rare_achievements = rare_achievements | in_both
    print(f"Rare achievements: {rare_achievements}\n")


def ft_achievement_tracker() -> None:
    """compares and prints different achievement statistics"""
    print("=== Achievement Tracker System ===\n")
    alice = Player("Alice", {"first_kill", "level_10", "treasure_hunter",
                             "speed_demon"})
    bob = Player("Bob", {"first_kill", "level_10", "boss_slayer", "collector"})
    charlie = Player("Charlie", {"level_10", "treasure_hunter", "boss_slayer",
                                 "speed_demon", "perfectionist"})
    alice.print_achievements()
    bob.print_achievements()
    charlie.print_achievements()
    print()
    print("=== Achievement Analytics ===")
    print_all_achievements(alice.get_achievements(), bob.get_achievements(),
                           charlie.get_achievements())
    print_common_achievements(alice.get_achievements(), bob.get_achievements(),
                              charlie.get_achievements())
    print_rare_achievements(alice.get_achievements(), bob.get_achievements(),
                            charlie.get_achievements())
    print(f"Alice vs Bob common: "
          f"{alice.get_achievements() & bob.get_achievements()}")
    print(f"Alice unique: {alice.get_achievements() - bob.get_achievements()}")
    print(f"Bob unique: {bob.get_achievements() - alice.get_achievements()}")


if __name__ == "__main__":
    ft_achievement_tracker()
