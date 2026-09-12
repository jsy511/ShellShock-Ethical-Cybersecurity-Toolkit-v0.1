"""
ShellShock Network Module
Safe networking utilities for learning.
"""

import ipaddress
import socket


def ip_info():
    """Show information about an IP address."""
    address = input("Enter an IP address: ").strip()

    try:
        ip = ipaddress.ip_address(address)

        print("\n--- IP Information ---")
        print(f"Address:  {ip}")
        print(f"Version:  IPv{ip.version}")
        print(f"Private:  {ip.is_private}")
        print(f"Loopback: {ip.is_loopback}")
        print(f"Global:   {ip.is_global}")

    except ValueError:
        print("[!] That isn't a valid IP address.")


def dns_lookup():
    """Resolve a hostname using the normal DNS resolver."""
    hostname = input("Enter a hostname: ").strip()

    try:
        address = socket.gethostbyname(hostname)

        print("\n--- DNS Result ---")
        print(f"Hostname: {hostname}")
        print(f"Address:  {address}")

    except socket.gaierror:
        print("[!] Could not resolve that hostname.")


def network_menu():
    """Display the Network module menu."""
    while True:
        print("\n=== ShellShock / Network ===")
        print("[1] IP information")
        print("[2] DNS lookup")
        print("[0] Back")

        choice = input("\nNetwork > ").strip()

        if choice == "1":
            ip_info()

        elif choice == "2":
            dns_lookup()

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")


if __name__ == "__main__":
    network_menu()