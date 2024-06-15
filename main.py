#!/bin/python

# Import module
try:
    from colorama import Fore, Style, Back
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
parser.add_argument('-iP', '--ip', help="entre the ip address to attack", dest='ip')
args = parser.parse_args()
c_ip = args.ip

# Send TCP query
def all_port(host):
    f = open(path+"WMAP_"+today, "w")
    SYNACK = 0x12
    port = 0
    try:
        print(Back.RED+"[?] CTRL+C to stop the script\n"+Back.RESET)
        print(Fore.LIGHTYELLOW_EX+"Port open: "+Fore.RESET)
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
os.system('cls' if os.name == 'nt' else 'clear')
deco = open("decoration.txt", "r")
print(Fore.LIGHTMAGENTA_EX + deco.read() + "\n" + Fore.RESET)

# Call function
if __name__ == '__main__':
    all_port(c_ip)