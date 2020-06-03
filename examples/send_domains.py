# -*- coding: utf-8 -*-
import sys
from acunetix import Acunetix

try:
    if len(sys.argv) > 1:
        domainz = sys.argv[1]
    else:
        print("using : {sys.argv[0]} domains.txt ")
        exit()
    
    z = open(domainz, 'r').read().splitlines()
    HOSTS = list(set(z))
except IOError:
    pass

server = Acunetix(host="", api="")

for domain in HOSTS:
    f = server.start_scan(address=domain)
    print(f)