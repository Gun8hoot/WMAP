# **WMAP**
---
## What is this script ?
- WMAP is a NMAP like tool write in python 3
- This script is a little slower because it scan all ports from 1 to 56535th port.

## Requirements
---
- To use this script you will need to install two python module called **argparse** & **scapy**

### Install module on Linux
- `pip3 install -r ./requirements.txt`\
or
- ```pip3 install argparse && pip3 install scapy```

### Install module on Windows
- `py -3 -m pip install argparse ` \
- `py -3 -m pip install scapy`

## How to use ?
---
- To used this script you will need to execute the **main.py** in sudoneers for Linux or administrator on Windows
- When we dont specify the IP to attack, the script scan automatically the loopback network interface (loopback=127.0.0.1)

### Execute on Linux
- `chmod +x ./main.py`\
- `sudo ./main.py -iP/--ip <target IP>` 

### Execute on Windows
- Run cmd with administrator privileges
- `py -3 main.py -iP/--ip <target IP> `
