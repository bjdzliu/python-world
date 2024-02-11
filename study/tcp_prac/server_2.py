import  socket
import subprocess

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8091))

phone.listen(5)
print("server is listening")


# wait connect
conn,client_addr=phone.accept()
print(conn)
print('client\'s ip and port ',client_addr)

while True:
    #receive data
    data=conn.recv(1024)  # max receviable data
    if len(data)==0: break
    obj=subprocess.Popen(data,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    res=obj.stdout.read()
    outinfo, errinfo=obj.communicate()
    
    print("client's msg is",res.decode('utf-8'))
    conn.send(res)

# close connection
conn.close()

# stop server

