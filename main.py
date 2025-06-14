import os, time, sys, threading
from module.color import color
from module.scanner import scan
from module.getHelp import getHelp
from module.logs import create_logs
from module.checkroot import checkroot

log_filename = "WMAP_" + time.strftime('%H-%M_%d-%m-%Y')
path = 'logs/'

banner = r"""
     █     █░ ███▄ ▄███▓ ▄▄▄       ██▓███  
    ▓█░ █ ░█░▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
    ▒█░ █ ░█ ▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
    ░█░ █ ░█ ▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
    ░░██▒██▓ ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
    ░ ▓░▒ ▒  ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
      ▒ ░ ░  ░  ░      ░  ▒   ▒▒ ░░▒ ░     
      ░   ░  ░      ░     ░   ▒   ░░       
        ░           ░         ░  ░         """


try: 
    os.makedirs(path)
except FileExistsError:
    pass


def main():
    arg_ip = ""
    arg_port = 0

    print(color.fr_orange + banner + color.reset)
    create_log = open(path + log_filename, "w")
    create_log.write(banner + "\n")

    try:
        checkroot()
        for x in sys.argv:
            if x.count('.') >= 2:
                arg_ip = x
                continue
            elif x.islower and x.count('/'):
                arg_port = x
                continue
            elif x.split("-") and len(x) >= 3:
                arg_port = x 
                continue
            elif x == "-h":
                getHelp()
                sys.exit()

        create_log.write(f"        ----- Scanning {arg_ip} -----\n")
        if arg_port == 0 or arg_port == "-p":
            create_log.write(f"{time.strftime('%H:%M:%S')} : [+] Scanning from port 1 to 65536\n")
            for p in range(65536):
                scan(arg_ip, p, create_log)
            
        elif str(arg_port).count("/") >= 1:
            with open(arg_port) as f:
                plist = f.readlines()
            create_log.write(f"{time.strftime('%H:%M:%S')} : [+] Scanning port from {str(arg_port)}\n")
            for lines in plist:
                scan(arg_ip, int(lines), create_log)
            
        elif arg_port.split("-") :
            arg_port = arg_port.split("-")
            arr = []
            arr.append(int(arg_port[0]))  
            arr.append(int(arg_port[1]))  
            create_log.write(f"{time.strftime('%H:%M:%S')} : [+] Scanning port in a range of {arr[0]} to {arr[1]}\n")
            for x in range(arr[0], arr[1]):
                scan(arg_ip, x+1, create_log)

    except IndexError:
        getHelp()
        
    except KeyboardInterrupt:
        print("\n[!] Abording ...")
        sys.exit()

if __name__ == "__main__":
    main()