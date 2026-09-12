"""
ShellShock CTF Module
Capture-the-Flag learning utilities.
"""

import codecs
import string


def rot13():
    """Encode or decode text using ROT13."""
    text = input("Enter text: ")

    result = codecs.decode(text, "rot_13")

    print(f"\nResult: {result}")


def caesar_cipher():
    """Encode text using a Caesar shift."""
    text = input("Enter text: ")

    try:
        shift = int(input("Enter shift (0-25): "))
    except ValueError:
        print("[!] Shift must be a number.")
        return

    result = ""

    for char in text:
        if char.isalpha():
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            index = alphabet.index(char)
            result += alphabet[(index + shift) % 26]
        else:
            result += char

    print(f"\nResult: {result}")


def ctf_menu():
    """Display the CTF module menu."""
    while True:
        print("\n=== ShellShock / CTF ===")
        print("[1] ROT13")
        print("[2] Caesar cipher")
        print("[0] Back")

        choice = input("\nCTF > ").strip()

        if choice == "1":
            rot13()

        elif choice == "2":
            caesar_cipher()

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")


if __name__ == "__main__":
    ctf_menu()