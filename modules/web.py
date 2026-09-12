"""
ShellShock Web Module
Safe web-security utilities for learning.
"""

import urllib.request


def security_headers():
    """Check common HTTP security headers."""
    url = input("Enter a URL you are authorised to test: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "ShellShock/0.1"}
        )

        with urllib.request.urlopen(request, timeout=5) as response:
            headers = response.headers

            print("\n--- HTTP Security Headers ---")
            print(f"URL: {url}")
            print(f"Status: {response.status}\n")

            security_headers_list = [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Referrer-Policy",
                "Permissions-Policy",
            ]

            for header in security_headers_list:
                value = headers.get(header)

                if value:
                    print(f"[+] {header}: {value}")
                else:
                    print(f"[-] {header}: Not detected")

    except Exception as error:
        print(f"[!] Request failed: {error}")


def web_menu():
    """Display the Web module menu."""
    while True:
        print("\n=== ShellShock / Web ===")
        print("[1] Security headers")
        print("[0] Back")

        choice = input("\nWeb > ").strip()

        if choice == "1":
            security_headers()

        elif choice == "0":
            break

        else:
            print("[!] Invalid option.")


if __name__ == "__main__":
    web_menu()