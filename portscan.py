#!/usr/bin/python
import socket,sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


if len(sys.argv) <= 1:
        print(f"{Fore.YELLOW}Usage Mode: python portscan.py host")
else:

        for porta in range(1,65535):
                meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if meusocket.connect_ex((sys.argv[1], porta)) == 0:
                        print(f"{Fore.GREEN}Port {porta} Open :D"
