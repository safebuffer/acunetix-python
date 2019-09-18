from core import ACUX
import sys

API_KEY = ""
SERVER = "" # server:port format

if len(sys.argv) > 1:
    eee = open(sys.argv[1], 'r').read().splitlines()
    HOSTS = list((eee))
else:
    print("domains.txt required")
    exit()
    
acunetix = ACUX(host=SERVER,api=API_KEY,timeout=30)

for host in HOSTS:
    if 'http' in host:
        try:
            acunetix.add_and_start(host)
            print("sent {}".format(host))
        except:
            pass
