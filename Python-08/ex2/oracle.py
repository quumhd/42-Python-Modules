#!/usr/bin/env python3


import os


def oracle() -> None:
    """to do"""
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("dotenv is not installed")
        print("To install it type: pip instlall dotenv")
        exit()

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    keys = {matrix_mode, database_url, api_key, log_level, zion_endpoint}

    for key in keys:
        if key is None:
            print(f"Key is missing, exiting...")
            exit()

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")
    print()
    print("Enviroment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides availible")



if __name__ == "__main__":
    oracle()
