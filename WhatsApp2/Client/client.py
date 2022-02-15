import socket
from datetime import datetime
import errno
import sys

HEADER_LENGTH = 10

now = datetime.now()

localhost_IP = input("Informe o IP localhost do servidor: ")

IP = localhost_IP
PORT = 5000

my_username = input("Usuario: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket(var IPv4, var TCP)
client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:

	choose = int(input("Escolha\n1 Ler\n2 Editar"))
	while choose < 1 or choose > 2:
		print("Voce deve escolher entre ler e editar somente")
		choose = int(input("Escolha\n1 Ler\n2 Editar"))

	if choose == 1:
		message = ""  # reader
	elif choose == 2:
		message = input(f"{my_username} > ") #client

	if message:
		message = message.encode("utf-8")
		message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
		client_socket.send(message_header + message)

	try:
		while True:
			username_header = client_socket.recv(HEADER_LENGTH)

			if not len(username_header):
				print("Conexao encerrada pelo servidor!")
				sys.exit()
			username_length = int(username_header.decode("utf-8").strip())

			username = client_socket.recv(username_length).decode("utf-8")

			message_header = client_socket.recv(HEADER_LENGTH)

			message_length = int(message_header.decode("utf-8").strip())

			message = client_socket.recv(message_length).decode("utf-8")


			print(now, f": {username} > {message}")

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print(now,": ", 'Erro de leitura', str(e))
			sys.exit()
		continue

	except Exception as e:
		print(now,": ", 'Erro geral', str(e))
		sys.exit()