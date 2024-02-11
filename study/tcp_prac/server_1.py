import  socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8090))

phone.listen(5)
print("server is listening")

# wait connect
conn,client_addr=phone.accept()
print(conn)
print('client\'s ip and port ',client_addr)

#receive data
data=conn.recv(1024)  # max receviable data
print("client's msg is",data.decode('utf-8'))
conn.send(data.upper())

conn.close()

# stop server

