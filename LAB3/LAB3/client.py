import socket
import datetime
 

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressIP		= socket.gethostname()

serverAddressPort	= 9999

serverAddressConn   = (serverAddressIP, serverAddressPort)

bufferSize          = 1024

 

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 


UDPClientSocket.sendto(bytesToSend, serverAddressConn)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
print datetime.datetime.now()
print ''
print 'Unesi string'
print '>>>'

test = raw_input()

if test == 'aspira':
	print 'NEDOSTUPNO!'
if test != 'aspira':
	print "Unijeli ste: %s" %(test)