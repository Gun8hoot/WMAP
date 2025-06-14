import os, sys

def checkroot():
    euid = os.geteuid()
    if euid == 0:
        return
    else:
        print("[!] FATAL ERROR : YOU NEED TO BE IN SUPERUSER, TRY WITH SUDO AND THE RIGHT PERMISSION")
        sys.exit(1)