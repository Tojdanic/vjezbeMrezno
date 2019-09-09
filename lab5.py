import socket
import subprocess
import sys
from datetime import datetime

t1 = datetime.now()
print "Vrijeme pokretanja ovog programa: "
print t1

print "Program se izvodi na racunalu:"
hostname=socket.gethostname()
print "Host name: ", hostname
ip = socket.gethostbyname(hostname)
print "IP address: ", ip

print ""

remoteServer    = raw_input("Enter host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

firstPort  = raw_input("Enter first port: ")
lastPort  = raw_input("Enter last port: ")

print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

try:
    for port in range(int(firstPort),int(lastPort)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()
	
print "Skeniranje zavrseno!"