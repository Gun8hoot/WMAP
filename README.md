<h1 style="text-align: center">WMAP</h1>

WMAP is a port scanner write in ***`python3`*** with only build-in lib 

## TODO
- [x] Code the port range arguments filter 
- [x] Create logs file system
- [ ] Fix time bug in logs
- [ ] Detect filtred port
- [ ] Bypass WAF
- [ ] Use threading to speed up scan time. Create 2 thread , first thread who scan first 32767 port and a second who scan last 32767 port  

### Execute on Linux
- First install python3 
```bash
sudo apt install python3
```
- Clone the repository
```bash
git clone https://github.com/Gun8hoot/WMAP.git
```
- Go in the directory
```bash
cd WMAP
```
- Execute the script 
```bash
sudo ./main.py -i {RHOST} -p {./PORT LIST or RANGE1-RANGE2} # WORKS WITHOUT -p | YOU NEED TO RUN IN SUDO 
```

