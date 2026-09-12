"""
ShellShock Crypto Module
Cryptography and encoding utilities for learning.
"""

import base64
import hashlib


def hash_text():
    """Generate a hash from text."""
    text = input("Enter text to hash: ")

    print("\n--- Hashes ---")
    print(f"MD5:    {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1:   {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}")


def base64_encode():
    """Encode text using Base64."""
    text = input("Enter text: ")

    encoded = base64.b64encode(text.encode()).decode()

    print(f"\nBase64: {encoded}")


def base64_decode():
    """Decode Base64 text."""
    encoded = input("Enter Base64: ")

    try:
        decoded = base64.b64decode(encoded).decode()

        print(f"\nDecoded: {decoded}")

    except Exception:
        print("[!] Invalid Base64 data.")


def crypto_menu():
    """Display the Crypto module menu."""
    while True:
        print("\n=== ShellShock / Crypto ===")
        print("[1] Hash text")
        print("[2] Base64 encode")
        print("[3] Base64 decode")
        print("[0] Back")

        choice = input("\nCrypto > ").strip()

        if choice == "1":
            hash_text()

        elif choice == "2":
            base64_encode()

        elif choice == "3":
            base64_decode()

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")


if __name__ == "__main__":
    crypto_menu()