import socket
import sys
a
# Array de portas para serem verificadas
ports = [80, 443, 21, 22, 23, 25, 3306, 8080, 8000, 405, 404, 19, 18, 50, 2227]

# Abre o protocolo TCP e pega o IPV4 (ou um IPV4 personalizado por argumento)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escaneamento de portas
for ports in ports:
	if sock.connect_ex((sys.argv[1], ports)):
		print("Port", ports, "Open")
sock.close

'''
'''

# Comando: portscan.py + seu IP
# Exemplo: portscan.py 192.168.0.10