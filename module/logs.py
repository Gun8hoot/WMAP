import os, sys, time

log_filename = "WMAP_" + time.strftime('%H-%M_%d-%m-%Y')
path = 'logs/'

def create_logs(banner):
    create_log = open(path + log_filename, "w")
    create_log.write(banner)
