import socket, threading, sys, time
from module.getHelp import getHelp

time_now = time.strftime('%H:%M:%S')
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(ip, port, log):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            r = sk.connect_ex((ip, port))
            if r == 0:
                print(f"\x1b[38;5;10m[+] The port {port} is open\x1b[0m")
                log.write(f"{time_now} : [+] The port {port} is open\n")
        sk.close()
    except socket.gaierror:
        print("[!] You need to specify an host")
        getHelp()
        sys.exit()
