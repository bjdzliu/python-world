import socket
import time

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8091))

while True:
    msg=input(">:")
    if len(msg)==0 :continue
    phone.send(msg.encode('utf-8'))
    print("waitingrecv")
    data=phone.recv(1024)
    print(data.decode('utf-8'))

phone.close()

