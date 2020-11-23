import time

# Converte um número em seu hexadecimal
def hexa(decimal):
    return hex(decimal[2:]).zfill(3).encode("utf-16")

def deca(hexadecimal):
    return int("0x{}".format(hexadecimal), 16)

# Formatação de header pro cabeçalho
def formatUDP(haveNext, segmentation, message):
    flag = int(haveNext).encode("utf-16")
    index = str(segmentation).zfill(3).encode("utf-16")
    return flag + index + message

