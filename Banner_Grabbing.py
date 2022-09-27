#!/usr/bin/python
import socket,sys,colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

if len(sys.argv) <= 1:
        print(f"{Fore.YELLOW}Usage Mode: python Banner_Grabbing.py host")
else:

        print("Interagindo com Servico!")

        ip = sys.argv[1]
        porta = int(sys.argv[2])

        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        meusocket.connect((ip,porta))
        banner = meusocket.recv(1024)
        print(banner)

        print("Enviando Usuario")
        meusocket.send("USER C1PH3R\r\n".encode("UTF-8"))
        user = meusocket.recv(1024)
        print(user)

        print("Enviando Senha")
        meusocket.send("PASS 1598753\r\n".encode("UTF-8"))
        passs = meusocket.recv(1024)
        print(passs)
