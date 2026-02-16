#!/usr/bin/env python3


def ft_archive_creation() -> None:
    """creates a file and writes to it"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open("new_discovery.txt", "w") as f:
            print("Sotrage unit created successfully\n")
            f.write("[ENTRY 001] New quantum algorithm discovered\n")
            print("[ENTRY 001] New quantum algorithm discovered")
            f.write("[ENTRY 002] Efficiency increased by 357%\n")
            print("[ENTRY 002] Efficiency increased by 357%")
            f.write("[ENTRY 003] Archieved by Data Archivist Trainee\n")
            print("[ENTRY 003] Archieved by Data Archivist Trainee")
    except FileNotFoundError as e:
        print(e)
    else:
        print()
        print("Data inscription complete. Storage unti sealed")
        print("Archive 'new_discovery.txt' ready for long-term preserveration")


if __name__ == "__main__":
    ft_archive_creation()
