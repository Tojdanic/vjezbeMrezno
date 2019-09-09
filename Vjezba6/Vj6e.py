from local_machine_info import print_machine_info
from Queue import Queue
import socket
import subprocess
import sys
import datetime
import time
import os
import thread
import threading

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

print_machine_info()
vrime = datetime.date.today()
print vrime

		
subprocess.call('', shell=True)
remoteServer    = raw_input("Unesi host za skeniranje:")

try:
	remoteServerIP = socket.gethostbyname(remoteServer)
	print "Postojeca IP adresa"
except socket.error:
	print "Nepostojeca IP adresa"



port = 80
retry = 1
delay = 1

def isOpen(remoteServerIP, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                s.connect((remoteServerIP, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
			return False
        finally:
                s.close()

def checkHost(remoteServerIP, port):
        ipup = False
        for i in range(retry):
                if isOpen(remoteServerIP, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if checkHost(remoteServerIP, port):
        print remoteServerIP + " je aktivan!"
		

hostname = remoteServerIP
response = os.system("ping -c 1 " + hostname)
if response == 0:
	pingstatus = "Network Active"
else:
	pingstatus = "Network Error"
print hostname
print  pingstatus		

def ping(host):
    import subprocess, platform


    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    
    return subprocess.call(args, shell=need_sh) == 0



print(ping(remoteServerIP))


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((remoteServerIP, port))
        with print_lock:
            print('Port', port, 'je aktivan!')
        con.close()
    except:
        pass
	
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

user_i = raw_input("First port: ")
user_input = raw_input("Last port: ")
start =int(user_i)
end=int(user_input) 		
q = Queue()		
startTime = time.time()
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(start, end):
	q.put(worker)
q.join()

print('Potrebno vrime:', time.time() - startTime)