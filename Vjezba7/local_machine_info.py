import socket

def print_machine_info():
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	print "Host name: %s" % host_name
	print "IP address: %s" % ip_address
	host_name_ip = socket.gethostbyaddr("8.8.8.8")
	print host_name_ip
	
if __name__ == '__name__':
	print_machine_info()
	