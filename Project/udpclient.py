#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
# python .\udpclient.py

import socket
import time
import random

from auxiliar import formatUDP, deca

# Variáveis
file = open("file.txt", "r", encoding='utf-8-sig', errors="strict")
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
UDPClientSocket.sendto(
    "0000Loremipsumdolorsitamet,consecteturadipiscingelit".encode("utf-16"),
    serverAddressPort)
UDPClientSocket.recvfrom(bufferSize)
roundTripTime = time.time() - initialTime # 0.001 segundos
roundTripTime = 0.001 if roundTripTime==0 else roundTripTime
print("Round-Trip-Time: {}".format(roundTripTime))

# Algoritmo que maneja enviar e receber pacotes
receivedAcks = []
def sendPackage(message):
    UDPClientSocket.sendto(message, serverAddressPort)
    responseIndex = deca(UDPClientSocket.recvfrom(bufferSize)[0].decode("utf-16"))
    return responseIndex

def verify(receivedAcks):
    notReceivedPackages = []
    # PARA SIMULAR A PERDA DE PACOTES
    # if len(receivedAcks)  > 5:
    #     del receivedAcks[2]
    for i in range(1, len(receivedAcks)):
        if i not in receivedAcks:
            notReceivedPackages = notReceivedPackages + [i]
    return notReceivedPackages

def fastRetransmit(failedPackaged): 
    print("\n Fast Retrasnmit to packages {}".format(failedPackaged))
    # print("\n Fast Retrasnmit to packages: {}".format(packages))

# Algoritmo de Slow Start
def slowStart():
    global cwnd, index, receivedAcks
    while cwnd < threshold and index < len(packages):
        print("\nStarting new Slow Start loop. Pacotes restantes: {}".format(len(packages)-index))
        newAcks = []
        for i in range(cwnd):
            if index >= len(packages): 
                break
            message = formatUDP(True, index, packages[index])
            ack = sendPackage(message)
            print("Sending package {}/{}, ack: {}".format(i+1, cwnd, ack))
            newAcks.append(ack)
            index += 1
        receivedAcks = receivedAcks + newAcks
        failedAcks = verify(receivedAcks)
        if len(failedAcks) > 0:
            fastRetransmit(failedAcks)
        if len(newAcks) == cwnd:
            cwnd += cwnd
        else:
            cwnd = 1
        newAcks.clear
    print("Reached threshold!" if (cwnd>=threshold) else "Ended streaming!")

# Algoritmo Congestion Avoidance
def congestionAvoidance():
    global cwnd, index, receivedAcks
    while cwnd >= threshold and index < len(packages):
        print("\nStarting new Congestion Avoidance loop. Pacotes restantes: {}".format(len(packages)-index))
        newAcks = []
        for i in range(cwnd):
            print("Sending package {}/{}".format(i+1, cwnd))
            newAcks.append(sendPackage(formatUDP(True, index, packages[index])))
            index += 1
        if len(newAcks) == cwnd:
            cwnd += 1
        else:
            cwnd /= 2

# 
while index < len(packages):
    if cwnd < threshold:
        print("Slow start")
        slowStart()
    else:
        print("Congestion Avoidance")
        congestionAvoidance()



file.close()
