import time

file = open("book.txt", "r", encoding='utf8')
stringOfFile = str.encode(file.read())
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 1024
packages = [stringOfFile[i:i+bufferSize] for i in range (0, len(stringOfFile), bufferSize)]

for p in packages:
    time.sleep(0.05)
    print(p)
