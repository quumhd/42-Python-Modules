#!/usr/bin/env python3


import sys


def ft_stream_management() -> None:
    """shows the 3 different communication channels"""
    alert_channel = sys.stderr
    standart_channel = sys.stdout
    print("=== CVYER ARCHIVES - COMMUNICATION SYTEM ===")
    id = input("Input Stream active. Enter Archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    print()
    standart_channel.write(f"[STANDART] Archive status from {id}: {report}\n")
    alert_channel.write("[ALERT] System diagnostics: "
                        "Communication channels verified\n")
    standart_channel.write("[STANDART] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
