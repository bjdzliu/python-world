import socket
import time

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8090))

time.sleep(100)
phone.send("hello".encode('utf-8'))

data=phone.recv(1024)
print(data.decode('utf-8'))

phone.close()

