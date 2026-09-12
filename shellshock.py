#!/usr/bin/env python3

"""
ShellShock
Ethical Cybersecurity Toolkit
Version 0.1
"""

VERSION = "0.1"


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
    print(f"                 ShellShock v{VERSION}")
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


def main():
    show_banner()

    while True:
        show_menu()

        choice = input("ShellShock > ").strip()

        if choice == "1":
            print("\n[Network] Module coming soon...\n")

        elif choice == "2":
            print("\n[Web] Module coming soon...\n")

        elif choice == "3":
            print("\n[Crypto] Module coming soon...\n")

        elif choice == "4":
            print("\n[Forensics] Module coming soon...\n")

        elif choice == "5":
            print("\n[CTF] Module coming soon...\n")

        elif choice == "6":
            print("\nShellShock is designed for ethical cybersecurity")
            print("learning and authorised testing only.\n")

        elif choice == "0":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n[!] Invalid option.\n")


if __name__ == "__main__":
    main()