#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket

# Variáveis
msgToClient = "Hello From UDP Client"
bytesToSend = str.encode(msgToClient)
serverAddressPort = ("127.0.0.1",8184)
bufferSize = 1024

# Criando Socket UDP do cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviando mensagem ao Servidor
UDPClientSocket.sendto(bytesToSend,serverAddressPort)

# Pegando mensagem do Servidor
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Mensagem do Servidor: {}".format(msgFromServer[0]))