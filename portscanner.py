#!/usr/bin/env python
import socket
import sys

remoteIPInput = raw_input("Host to scan: ")
remoteIP = socket.gethostbyname(remoteIPInput)

print "Scanning host", remoteIP

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((remoteIP, port))
        sock.settimeout(None)
        if result == 0:
            print "Port "+ str(port) + " Open!"
        sock.close()

except KeyboardInterrupt:
    print "Stopped"
    sys.exit()
