#!/usr/bin/env python3


import os
import sys


def loading() -> None:
    """demonstrates loading external librarys"""
    print("LOADING STATUS: Loading programs...\n")
    print("Check for dependencies:")
    all_dependencies = True
    try:
        import numpy as np
        print(f"[OK] numpy {np.__version__} - Data manipulation ready")
    except ImportError:
        print("[KO] numpy has not been installed properly")
        all_dependencies = False
    try:
        import pandas
        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    except ImportError:
        print("[KO] pandas has not been installed properly")
        all_dependencies = False
    try:
        import requests
        print(f"[OK] requests {requests.__version__} - Data manipulation ready")
    except ImportError:
        print("[KO] requests has not been installed properly")
        all_dependencies = False
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        print(f"[OK] matplotliob {matplotlib.__version__} - Data manipulation ready")
    except ImportError:
        print("[KO] matplotlib has not been installed properly")
        all_dependencies = False
    if all_dependencies == False:
        print()
        print("Missing dependencies, exiting the program...")
        return
    print()
    print("Analysing Matrix data...")
    np.random.seed(0)
    rows, cols = 100, 100
    matrix_data = np.random.rand(rows, cols) * 100
    print("Processing 10000 data points")
    print("Generating visualisation")
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix_data)
    plt.colorbar()
    print()
    plt.savefig('matrix_heatmap.png')
    plt.close()
    print("Analysis complete")
    print(f"Result saved to: matrix_heatmap.png")


if __name__ == "__main__":
    loading()
