#!/usr/bin/env python3

"""
ShellShock
Ethical Cybersecurity Toolkit
Version 0.1.0
"""

import config
from modules.network import network_menu
from modules.web import web_menu
from modules.crypto import crypto_menu
from modules.forensics import forensics_menu
from modules.ctf import ctf_menu


LOGO = r"""
███████╗██╗  ██╗███████╗██╗     ██╗         ███████╗██╗  ██╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██║  ██║██╔════╝██║     ██║         ██╔════╝██║  ██║██╔═══██╗██╔═══╝██║ ██╔╝
███████╗███████║█████╗  ██║     ██║         ███████╗███████║██║   ██║██║     █████╔╝
╚════██║██╔══██║██╔══╝  ██║     ██║         ╚════██║██╔══██║██║   ██║██║     ██╔═██╗
███████║██║  ██║███████╗███████╗███████╗    ███████║██║  ██║╚██████╔╝╚██████╗██║  ██╗
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""


def show_banner():
    print(LOGO)
    print(f"                 {config.NAME} v{config.VERSION}")
    print("          Ethical Cybersecurity Toolkit")
    print()


def show_menu():
    print("[1] Network")
    print("[2] Web")
    print("[3] Crypto")
    print("[4] Forensics")
    print("[5] CTF")
    print("[6] Help")
    print("[0] Exit")
    print()


def show_help():
    print("\n=== ShellShock Help ===")
    print(config.DESCRIPTION)
    print()
    print("Use ShellShock only for learning, CTFs,")
    print("and systems you are authorised to test.")
    print()


def main():
    show_banner()

    while True:
        show_menu()

        choice = input("ShellShock > ").strip()

        if choice == "1":
            network_menu()

        elif choice == "2":
            web_menu()

        elif choice == "3":
            crypto_menu()

        elif choice == "4":
            forensics_menu()

        elif choice == "5":
            ctf_menu()

        elif choice == "6":
            show_help()

        elif choice == "0":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n[!] Invalid option.\n")


if __name__ == "__main__":
    main()