#!/usr/bin/python
import socket,sys


print('\033[1;31m/' * 80)
print('\033[1;31m/', ' ' * 25, 'STUDENT: C1PH3R-UNKN0W', ' ' * 27, '\033[1;31m/')
print('\033[1;31m/' * 80)

#if len(sys.argv) <= 2:

#       print("Use mode: arg.py host port")
#       print("Example usage: python arg.py 10.0.0.1 8080")
#else:
#       print("Varrendo o host:", (sys.argv[1]), "na porta:", (sys.argv[2]))

#for ip in range(1,255+1):
#       print(f"Varrendo IP: 192.168.0.{ip}")


if len(sys.argv) <= 2:
        print("\n\033[1;97mUse mode: script.py host port")
        print("\n\033[1;97mExample usage: python script.py 127.0.0.1 8080")
else:
        ip = sys.argv[1]
        porta = int(sys.argv[2])

        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = meusocket.connect_ex((ip, porta))

        if (res == 0):
                print("\n\033[1;32mPorta Aberta :D")
        else:
                print("\n\033[1;31mPorta Fechada :(")
