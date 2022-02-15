import socket
import sys

ports = [80, 443, 21, 22, 23, 25, 3306, 8080, 8000, 405, 404, 19, 18, 50, 2227]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for ports in ports:
	if sock.connect_ex((sys.argv[1], ports)):
		print("Port", ports, "Open")
sock.close