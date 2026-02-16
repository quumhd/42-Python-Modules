#!/usr/bin/env python3


def ft_vault_security() -> None:
    """read and write to files with the "width" keyword"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initialising secure vault access")
    with open("classified_data.txt", "r") as f:
        with open("classified_data_preservation.txt", "w") as p:
            print("Vault connection established with failsave protocols\n")
            print("SECURE EXTRACTION:")
            for line in f:
                print(line, end="")
                p.write(line)
            print("\n")
            print("SECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archives")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security")


if __name__ == "__main__":
    ft_vault_security()
