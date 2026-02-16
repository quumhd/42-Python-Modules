#!/usr/bin/env python3


def ft_crisis_response() -> None:
    """handles files with errors"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r"):
            print("connection established")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, system stable")
    print()
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r"):
            print("connection establised")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")
    print()
    try:
        print("ROUTINE ACCESS:  Attempting access to 'standart_archive.txt'...")
        with open("standart_archive.txt") as f:
            print(f"SUCCESS: Archive recovered - '{f.readlines}'")
    except FileNotFoundError:
        print("STATUS: Crisis handled, security maintained")
    except PermissionError:
        print("RESPONE: Security protocols deny access")
    finally:
        print("STATUS: Normal operations resumed")
    print()
    print("All crisis scenatios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
