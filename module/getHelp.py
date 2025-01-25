from module.color import color

with open('./banner', 'r') as banner:
    banner = banner.read()

def getHelp() : 
    print("\n WMAP port scanner:")
    print("   -h : Print this message")
    print("   -i : The IP address of the target")
    print("   -p : The range of port to scan or a file with port to scan [keep blank to scan every port]")