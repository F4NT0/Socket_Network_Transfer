import time

file = open("book.txt", "r", encoding='utf-8', errors="strict")
stringOfFile = file.read().encode("utf-16", errors="replace")
serverAddressPort = ("127.0.0.1", 8184)
bufferSize = 1024
packages = [stringOfFile[i:i+bufferSize] for i in range (0, len(stringOfFile), bufferSize)]

for p in packages:
    time.sleep(0.01)
    print(p.decode('utf-16'))

file.close()
