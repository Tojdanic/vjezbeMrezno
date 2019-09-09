import socket
import struct
import sys

from local_machine_info import print_machine_info 

multicast_group = '224.51.24.9'
server_address = ('', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
	print >>sys.stderr, '\nwaiting to receive message'
	data, address = sock.recvfrom(1024)
	print >>sys.stderr,'received "%s" bytes from "%s"'%(len(data),address)
	print>>sys.stderr,dataprint>>sys.stderr,'sending acknowledgement to',address
	sock.sendto('ack',address)