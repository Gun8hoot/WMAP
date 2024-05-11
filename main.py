#!/bin/python

# Import module
try:
    from colorama import Fore, Style
except ValueError:
    pass
import argparse, os, time
from scapy.all import *
import sys 
from logging import getLogger, ERROR

getLogger("scapy.runtime").setLevel(ERROR)

# General vars
today = time.strftime('%H-%M_%d-%m-%Y')
path = "report/"
port = 0

# Creating the report directory
try: 
    os.makedirs(path)
except FileExistsError:
    pass

# Arguments vars
parser = argparse.ArgumentParser(prog='WMAP',description='NMAP version who hold with a thread')
ip = parser.add_argument('-iP', '--ip', help="entre the ip address to attack")
args = parser.parse_args()
c_ip = args.ip

# Send ICMP query
def ping(host):
    ans, unans = sr(IP(dst=host)/ICMP(), timeout=3)
    try:
        ans.summary(lambda s,r: r.sprintf(Fore.RESET + Fore.GREEN + "\n\n    [+] %IP.src% is alive") + Fore.RESET)
    except KeyboardInterrupt:
        print(Fore.RED + Style.DIM + "\n[!] The script has been interupt by the user" + Style.RESET_ALL)
        sys.exit(0)

# Send TCP query
def all_port(host):
    f = open(path+"WMAP_"+today, "w")
    SYNACK = 0x12
    port = 0
    try:
        print("\nPort open: ")
        while port != 56535:
            SYNACK_request = sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
            if SYNACK_request is not None:
                tcp_request = SYNACK_request.getlayer(TCP).flags
                if tcp_request == SYNACK:
                    print(Fore.GREEN + "    [+] The port %s is open" % port + Fore.RESET)
                    f.writelines([" [+] The port %s is open\n" % port])
                else:
                    pass
            else:
                pass
            port += 1
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] The script has been interupt by the user" + Style.RESET_ALL)
        sys.exit(0)

# Decoration
deco = open("decoration.txt", "r")
print(Fore.LIGHTMAGENTA_EX + deco.read() + "\n" + Fore.RESET)

# Call function
ping(c_ip)
all_port(c_ip)