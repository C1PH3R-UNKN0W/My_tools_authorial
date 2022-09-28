#!/usr/bin/python
import socket,sys,colorama,requests
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print('\033[1;31m/' * 80)
print('\033[1;31m/', ' ' * 25, 'STUDENT: C1PH3R-UNKN0W', ' ' * 27, '\033[1;31m/')
print('\033[1;31m/' * 80)

if len(sys.argv) <= 1:
        print(f"{Fore.YELLOW}\nUsage Mode: python resolver.py host")

else:

        try:
                host = sys.argv[1]
                green = socket.gethostbyname(host)
                plus = "[+]"
                print(f'\n{Fore.GREEN} {plus} {host}', "\x1B[31m --->",(f'{Fore.GREEN} {green}'))
        except:
                print("\n\x1B[31m[-] Domain error, try again!")
