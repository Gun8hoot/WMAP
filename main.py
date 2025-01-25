import os, time, sys, threading
from module.color import color
from module.scanner import scan
from module.getHelp import getHelp

today = time.strftime('%H-%M_%d-%m-%Y')
path = "logs/"
arg_ip = 0
arg_port = 0

try: 
    os.makedirs(path)
except FileExistsError:
    pass

with open('./banner', 'r') as banner:
    banner = banner.read()

def main(arg_ip, arg_port):
    print(color.fr_orange + banner + color.reset + "\n")
    try:
        for x in sys.argv:
            if x.count('.') >= 2:
                arg_ip = x
                continue
            elif x.islower and x.count('/'):
                arg_port = x
                continue
            elif x == "-h":
                getHelp()
                sys.exit()
        if arg_port == 0:
            for p in range(65536):
                scan(arg_ip, p)
        elif str(arg_port).count("/") >= 0:
            with open(arg_port) as f:
                plist = f.readlines()
            for lines in plist:
                scan(arg_ip, int(lines))
            
    except IndexError:
        getHelp()
    except KeyboardInterrupt:
        print("\n[!] Abording ...")
        sys.exit()

if __name__ == "__main__":
    main(arg_ip,arg_port)

