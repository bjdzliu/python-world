import  socket
import logging
logging.basicConfig(format='%(thread)s %(threadName)s %(message)s ',level=logging.INFO)

## 创建一个socket对象
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip='127.0.0.1'
port=8090
addr=(ip,port)

phone.bind(addr)  #2

#启动监听
phone.listen()
logging.info("server is listening")

# wait connect
conn,client_addr=phone.accept() #默认是阻塞的
logging.info(conn)
logging.info(client_addr)


#receive data
data=conn.recv(1024)  # max receviable data
print("client's msg is",data.decode('utf-8'))

# byte data
msg="ack {}".format(data.decode())
conn.send(msg.encode())
#conn.send(data.upper())

logging.info(phone)

conn.close()
phone.close()
# stop server

