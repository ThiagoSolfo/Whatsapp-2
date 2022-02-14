import socket
import select

escolha = input("\nDigite 1 para \"server\" ou 2 para \"client\":\n")
 
if escolha == "1":
    HEADER_LENGTH = 10
    IP = "127.0.0.1"
    PORT = 8080

    server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((IP, PORT))

    server_socket.listen()

    sockets_list = [server_socket]

    clients = {}
elif escolha == "2":
    print("Você escolheu \"client\"!")
else:
    print("Escolha errada, terminando programa.")

