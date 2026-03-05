#!/usr/bin/env python3


import os
import sys
import site


def is_virtual_env() -> bool:
    """checks if program is running in virutal env"""
    return 'VIRTUAL_ENV' in os.environ


def construct() -> None:
    """shows information based on the enviroment"""
    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct\n")
        env_path = os.getenv('VIRTUAL_ENV')
        env_name = os.path.basename(env_path)
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Enviroment: {env_name}")
        print(f"Enviroment path: {env_path}")
        print()
        print("SUCESS: You're in a virtual enviroment!")
        print("Safe to install packages without effecting the global system.")
        print()
        print(f"Package installtion path:\n{site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Pyhton: {sys.executable}")
        print("Virtual Enviroment: None detected")
        print()
        print("WARNING: You're in the global enviroment")
        print("The machine can see everything you install")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate   # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run the program again")
        




if __name__ == "__main__":
    construct()
