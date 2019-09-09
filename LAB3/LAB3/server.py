import socket
import datetime
from local_machine_info import print_machine_info 
 

IP     = socket.gethostname()
Port   = 9999
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

 

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 



UDPServerSocket.bind((IP, Port))

 

print("UDP server up and listening")
print datetime.datetime.now()
print_machine_info ()




while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
	
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   


    UDPServerSocket.sendto(bytesToSend, address)