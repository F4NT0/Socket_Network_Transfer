import time

# cd Desktop/LabRedes/TF/Socket_Network_Transfer/Project
# python .\udpclient.py

# Converte um número em seu hexadecimal
def hexa(decimal):
    return hex(decimal)[2:].zfill(3)
#
def deca(hexadecimal):
    return int("0x{}".format(hexadecimal), 16)

# Formatação de header pro cabeçalho
def formatUDP(haveNext, segmentation, message):
    flag = str(int(haveNext))
    index = str(segmentation).zfill(3)
    return (flag + index).encode("utf-16") + message

