Primeiro, importar o socket
Segundo, definir o objeto socket

(socket.AF_INET corresponde ao endereço Ipv4 e socket.SOCK_STREAM corresponde ao TCP)

s.bind() = Vincular o socket a uma tupla(lista) de hosts
a tupla estará nesse caso por conta de termos um IP e uma porta

Temos um server e precisamos hospeda-lo

socket.gethostname() e uma porta 1234(qualquer sequência numérica)
Os dígitos mais baixos geralmente estarão ocupados por outros programas

Vc usa o soquete para comunicação, mas ele não é a comunicação em si, é apenas o ponto final
Como ele recebe essa conexão no ponto final, fica em um IP e um port

Vamos fazer conexão agora, para tanto precisamos que nosso servidor esteja preparado para receber
essas conexões de entrada vamos colocar uma fila de 5, então se o server estiver sob carga
pesada e como várias conexões chegam rapidamente elas começam a se acumular, então teremos uma
fila de 5(cinco conexões simultâneas(se 6 pcs se conectarem ao mesmo tempo o servidor não vai
responder basicamente))
s.listen(5)

agora, logica básica enquanto for true eu escuto

while True:
	o nosso clientsocket no endereço tal vai ser aceito
	Oq significa que o client será escutado enquanto for verdadeiro
	
	clientsocket, adrres = s.accept()

	aqui armazenamos o nosso objeto "s" no clientsocket e então o endereço é 
de onde eles estão vindo, logo isso agirá como um endereço IP

próxima etapa é debugar uma mensagem de conexão 

print(f"Connection from {address} has been estabilished!")

em seguida vamos enviar a mensagem em bytes usando

clientsocket.send(bytes("msg", "decriptação geralmente utf-8"))

isso tudo em "server.py"

em "client.py"

fazemos a mesma atribuição de "s" e passamos s.connect com socket.gethostname e uma porta

em seguida armazenamos em uma variavel o conteúdo recebido com um buffer de 1024b
e printamos na tela a mensagem no server usando variavel.decode("utf-8))

----------------------------------------------------------------------------------------------
abra o cmd na mesma pasta onde está salvo o client.py e o server.py

incialize o server digitando 

py -"versão python instalada ou 3.7 ou 3.10" 3.10 server.py

abra outro cmd e digite

py -3.10 client.py

e pronto

------------------------------------------------------------------------------------------------

msg = s.recv(int buffer)

buffer é o nosso fluxo e para recebermos mensagem precisamos decidir quão grandes serão os "pedaços" de informações que o server vai receber por vez


Quando você excede esse buffer a mensagem exibida não será a mensagem em seu tamanho real por exemplo a mensagem "Welcome to the server!" se tivermos 1024b de buffer a mensagem é exibida é "Welcome to the server!" se tivermos 8b de buffer a mensagem exibida é "Welcome" ou seja 90% cortada


