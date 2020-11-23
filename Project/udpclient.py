#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket
import time
import random

from auxiliar import formatUDP

# Variáveis
file = open("file.txt", "r", encoding='utf-8', errors="strict")
encodedStr = file.read().encode("utf-16", errors="replace")
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 290
packages = [encodedStr[i:i+bufferSize] for i in range (0, len(encodedStr), bufferSize)]

# Variáveis para mandar pacotes
cwnd = 1 # congestion avoidance
threshold = 64
mtu = 1500
mss = mtu - 40 # maximum segment size
roundTripTime = -1 #rtt
index = 0

# Criando Socket UDP do cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Verificando RTT
initialTime = time.time()
# UDPClientSocket.sendto(
#     "0000Loremipsumdolorsitamet,consecteturadipiscingelit".encode("utf-16"),
#     serverAddressPort)
# UDPClientSocket.recvfrom(bufferSize)
roundTripTime = time.time() - initialTime # 0.001 segundos
roundTripTime = 0.001 if roundTripTime==0 else roundTripTime
print("Round-Trip-Time: {}".format(roundTripTime))

# Algoritmo de Slow Start
def slowStart():
    global cwnd, index
    while cwnd < threshold and index < len(packages):
        for i in range(cwnd):
            if index >= len(packages): 
                break
            UDPClientSocket.sendto(
                formatUDP(True, index, packages[index]),
                serverAddressPort)
            UDPClientSocket.recvfrom(bufferSize)
            index += 1
        cwnd += cwnd
    print("Reached threshold!" if (cwnd>=threshold) else "Ended streaming!")

# Algoritmo Congestion Avoidance
def congestionAvoidance():
    global cwnd, index
    while cwnd >= threshold and index < len(packages):
        UDPClientSocket.sendto(
            formatUDP(True, index, packages[index]),
            serverAddressPort)
        UDPClientSocket.recvfrom(bufferSize)
        index += 1
        cwnd += 1

# 
while index < len(packages):
    if cwnd < threshold:
        print("Slow start")
        slowStart()
    else:
        print("Congestion Avoidance")
        congestionAvoidance()



file.close()
