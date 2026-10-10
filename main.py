#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from modules.utils import Colors, banner, get_platform, clear

# Modüller
from modules import osint, bruteforce, network, webscan, ai_helper

def print_menu():
    clear()
    banner()
    print(f"""{Colors.GREEN}
╔══════════════════════════════════════════════════════════════╗
║                      MAIN MENU                               ║
╠══════════════════════════════════════════════════════════════╣
║  {Colors.WHITE}[1]{Colors.GREEN}  OSINT Intelligence                                    ║
║  {Colors.WHITE}[2]{Colors.GREEN}  Brute Force Attacks                                   ║
║  {Colors.WHITE}[3]{Colors.GREEN}  Network Utilities                                     ║
║  {Colors.WHITE}[4]{Colors.GREEN}  Web Scanning                                          ║
║  {Colors.WHITE}[5]{Colors.GREEN}  AI Assistant                                          ║
║  {Colors.WHITE}[6]{Colors.GREEN}  Payload Generator                                     ║
║  {Colors.WHITE}[7]{Colors.GREEN}  Password Tools                                        ║
║  {Colors.WHITE}[8]{Colors.GREEN}  Social Engineering                                    ║
║  {Colors.WHITE}[9]{Colors.GREEN}  Cryptography Tools                                    ║
║  {Colors.WHITE}[10]{Colors.GREEN} System Information                                    ║
║  {Colors.WHITE}[0]{Colors.GREEN}  Exit                                                 ║
╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}""")

def main():
    while True:
        print_menu()
        choice = input(f"{Colors.GREEN}[LYRESX]{Colors.WHITE} Select option: {Colors.RESET}").strip()
        
        if choice == "1":
            osint.menu()
        elif choice == "2":
            bruteforce.menu()
        elif choice == "3":
            network.menu()
        elif choice == "4":
            webscan.menu()
        elif choice == "5":
            ai_helper.menu()
        elif choice == "6":
            print(f"{Colors.YELLOW}[*] Payload Generator coming soon...{Colors.RESET}")
            time.sleep(2)
        elif choice == "7":
            print(f"{Colors.YELLOW}[*] Password Tools coming soon...{Colors.RESET}")
            time.sleep(2)
        elif choice == "8":
            print(f"{Colors.YELLOW}[*] Social Engineering coming soon...{Colors.RESET}")
            time.sleep(2)
        elif choice == "9":
            print(f"{Colors.YELLOW}[*] Cryptography Tools coming soon...{Colors.RESET}")
            time.sleep(2)
        elif choice == "10":
            print(f"{Colors.YELLOW}[*] System Information coming soon...{Colors.RESET}")
            time.sleep(2)
        elif choice == "0":
            print(f"{Colors.RED}[!] Exiting...{Colors.RESET}")
            sys.exit(0)
        else:
            print(f"{Colors.RED}[!] Invalid option!{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
