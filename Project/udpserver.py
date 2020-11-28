#
# UDP Server
# no terminal: python3 udpserver.py
# Rode ele primeiro em um terminal separado
#

import socket
from time import sleep
from auxiliar import hexa, deca

# Variáveis
serverIP = "127.0.0.1"
localPort = 8184
bufferSize = 300

# Criando um Datagram Socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Definindo (bind) com o ip e porta
UDPServerSocket.bind((serverIP,localPort))

# Mensagem mostrando que está ativo
print("UDP Server UP and LISTENING!\n")

# Esperando por qualquer Datagram para o Servidor
try:
    while(True):
        # Recebendo mensagem do Cliente
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        input = bytesAddressPair[0].decode('utf-16')
        address = bytesAddressPair[1]

        # Verifica se pacote recebido é menor do que deveria ser
        if len(input) < 4:
            continue

        # Getting input segment and message
        segment = input[0:4]
        message = input[4:]

        # Apresentação da Mensagem
        print("Recebido pacote{} do cliente.".format(" único" if segment[0] == '0' else ""))
        print("IP: {}, porta: {}".format(address[0], address[1]))

        # Verifica se a mensagem é única ou se outras irão vir
        if segment[0] == '0':
            print("Message:\t{}".format(message))
            # Deleta conteúdo do arquivo a ser escrito
            f = open("fileCopied.txt", "w", encoding="utf-8-sig")
            f.write("")
            f.close()
        else:
            print("Fragment with index: {}".format(deca(segment[1:])))
            print("Fragment size: {}".format(len(message)))

            # Guardando os dados em um arquivo
            f = open("fileCopied.txt", "a", encoding="utf-8-sig")
            f.write(message)
            f.close()

            print("Conteúdo do pacote foi adicionado com sucesso no arquivo fileCopied.txt")
        
        print("")
        sleep(0.5)

        # Enviando resposta ao Cliente
        UDPServerSocket.sendto( segment[1:].encode("utf-16"),address)

except Exception as socketException:
    print("\n========================")
    print("Server exception ocurred")
    print(socketException)
    print("========================")
finally:
    UDPServerSocket.close()
    print("\n========================")
    print("     Server closed")
    print("========================")

