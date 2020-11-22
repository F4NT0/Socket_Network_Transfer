#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket

# Variáveis
file = open("book.txt", "r", encoding='utf-8', errors="strict")
stringOfFile = file.read().encode("utf-16", errors="replace")
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 1024
packages = [stringOfFile[i:i+bufferSize] for i in range (0, len(stringOfFile), bufferSize)]

# Criando Socket UDP do cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviando mensagem ao Servidor
for package in packages:
    UDPClientSocket.sendto(package,serverAddressPort)

# Pegando mensagem do Servidor
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Mensagem do Servidor: {}".format(msgFromServer[0]))