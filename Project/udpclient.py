#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket
import time
import random

# Variáveis
file = open("book.txt", "r", encoding='utf-8', errors="strict")
encodedStr = file.read(100).encode("utf-16", errors="replace")
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 1024
packages = [encodedStr[i:i+bufferSize] for i in range (0, len(encodedStr), bufferSize)]

# Variáveis do Slow Start
cwnd = 1
threshold = 64
mtu = 1500
mss = mtu - 40
roundTripTime = -1

# Criando Socket UDP do cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Funções auxiliares de formatação do cabeçalho
def formatUDP(segmentation, message):
    return "{:04d}".format(int(segmentation)).encode("utf-16") + message

# Verificando RTT
initialTime = time.time()
UDPClientSocket.sendto(
    "0000Loremipsumdolorsitamet,consecteturadipiscingelit".encode("utf-16"),
    serverAddressPort)
UDPClientSocket.recvfrom(bufferSize)
roundTripTime = time.time() - initialTime # 0.001 segundos
roundTripTime = 0.001 if roundTripTime==0 else roundTripTime
print("Round-Trip-Time: {}".format(roundTripTime))


def slowStart():
    global cwnd
    while cwnd < threshold:
        for index in range(cwnd):
            UDPClientSocket.sendto()
    initialTime = time.time()

    print("Reached threshold!" if (cwnd>=threshold) else "Ended streaming!")



# Enviando mensagem ao Servidor
for package in packages:
    UDPClientSocket.sendto(package,serverAddressPort)
    # Pegando mensagem do Servidor
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Mensagem do Servidor: {}".format(msgFromServer[0]))

file.close()
