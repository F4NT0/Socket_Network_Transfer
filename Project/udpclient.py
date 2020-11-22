#
# UDP Client 
# no terminal: python3 udpclient.py
# Rode ele depois de iniciar em outro terminal o Servidor
#

import socket

# Variáveis
file = open("book.txt", "r", encoding='utf-8', errors="strict")
encodedStr = file.read().encode("utf-16", errors="replace")
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

def slowStart():
    global cwnd
    print("Starting slow start...")
    index = 0
    while cwnd < threshold:
        print("cwnd: " + cwnd)
        for aux in range(cwnd):
            UDPClientSocket.sendto(packages[index],serverAddressPort)
            index += 1
        socket.listen(cwnd)
        try:
            for i in range(cwnd):
                if socket.accept() == 0: raise Exception()
            cwnd += cwnd
        except:
            cwnd = 1

    print("Reached threshold!" if (cwnd>=threshold) else "Ended streaming!")



# Enviando mensagem ao Servidor
for package in packages:
    UDPClientSocket.sendto(package,serverAddressPort)
    # Pegando mensagem do Servidor
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Mensagem do Servidor: {}".format(msgFromServer[0]))

file.close()
