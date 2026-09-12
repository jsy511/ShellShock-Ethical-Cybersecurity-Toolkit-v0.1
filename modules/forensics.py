"""
ShellShock Forensics Module
Basic file-analysis utilities for learning.
"""

import hashlib
import os


def file_info():
    """Display basic information about a file."""
    path = input("Enter file path: ").strip()

    if not os.path.isfile(path):
        print("[!] File not found.")
        return

    size = os.path.getsize(path)

    print("\n--- File Information ---")
    print(f"Name: {os.path.basename(path)}")
    print(f"Size: {size} bytes")
    print(f"Path: {os.path.abspath(path)}")


def file_hash():
    """Calculate a SHA-256 hash for a file."""
    path = input("Enter file path: ").strip()

    if not os.path.isfile(path):
        print("[!] File not found.")
        return

    sha256 = hashlib.sha256()

    try:
        with open(path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        print("\n--- SHA-256 ---")
        print(sha256.hexdigest())

    except OSError as error:
        print(f"[!] Could not read file: {error}")


def forensics_menu():
    """Display the Forensics module menu."""
    while True:
        print("\n=== ShellShock / Forensics ===")
        print("[1] File information")
        print("[2] SHA-256 file hash")
        print("[0] Back")

        choice = input("\nForensics > ").strip()

        if choice == "1":
            file_info()

        elif choice == "2":
            file_hash()

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")


if __name__ == "__main__":
    forensics_menu()