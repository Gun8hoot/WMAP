import socket, threading, sys, time
from module.getHelp import getHelp

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            r = sk.connect_ex((ip, port))
            if r == 0:
                print(f"\x1b[38;5;10m[+] The port {port} is open\x1b[0m")
        sk.close()
    except socket.gaierror:
        print("[!] You need to specify an host")
        getHelp()
        sys.exit()
