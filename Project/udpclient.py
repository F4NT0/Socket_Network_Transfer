#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket

# Variáveis
file = open("file.txt", "r", encoding='utf-8', errors="strict")
encodedStr = file.read().encode("utf-16", errors="replace")
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 300
packages = [encodedStr[i:i+bufferSize] for i in range (0, len(encodedStr), bufferSize)]

# Criando Socket UDP do cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviando mensagem ao Servidor
i = 0
for package in packages:
    UDPClientSocket.sendto(package,serverAddressPort)
    # Pegando mensagem do Servidor
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Enviando pacote {}".format(i))
    print("Mensagem do Servidor: {}".format(msgFromServer[0]))
    i = i + 1


file.close()
