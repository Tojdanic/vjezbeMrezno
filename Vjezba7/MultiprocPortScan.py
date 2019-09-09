import socket
import datetime
import time
import multiprocessing
import sys
from local_machine_info import print_machine_info
import os

def scanner(arg):
	IP, portNo = arg
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	kon = tcp.connect_ex((IP, portNo))
	if kon == 0:
		return portNo, True
	else:
		return portNo, False
	tcp.close()
	
def pHandler(ports):
	noCPU = multiprocessing.cpu_count()
	print "No. of cores: %d \n Will use: %d" % (noCPU, noCPU*2)
	pool = multiprocessing.Pool(processes = noCPU*2)
	for port, status in pool.map(scanner, [(IP, port) for port in ports]):
		print "Skenira se port: %d" % port
		if status == True:
			print "Port %d je otvoren" % port
			
			
if __name__ == "__main__":
	print "Pokrece se:"
	print datetime.datetime.now()
	print "Podaci:"
	print_machine_info()
	print "Skeniraj:"
	host = raw_input(">> ")
	
	IP = socket.gethostbyname(host)
	print "Skenira se:\nhost: %s,\nIP: %s" % (host, IP)
	print "Provjera hosta: %s" % (host)
	pok = os.system('ping ' + IP + ' -n 1')
	if pok == 0:
		print "Host %s je dostupan" % host
		poc = int(raw_input("Pocetni port: "))
		end = int(raw_input("endnji port: "))
		
		ports = range(poc, end + 1)
		startTime = time.time()
		pHandler(ports)
		endTime = time.time()
		difference = endTime - startTime
		print difference