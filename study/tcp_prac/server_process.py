import  socket
import subprocess
import multiprocessing

## 在Linux上可以
## 在mac上报Address already in use

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

print("multi process will also do this")
phone.bind(('127.0.0.1',8091))

phone.listen(5)
print("server is listening")

def service_client(conn):
    #receive data
    data=conn.recv(1024)  # max receviable data
    if len(data)==0: return None
    obj=subprocess.Popen(data,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    res=obj.stdout.read()
    outinfo, errinfo=obj.communicate()
    
    print("client's msg is",res.decode('utf-8'))
    conn.send(res)
    conn.close()


while True:
    # wait connect
    conn,client_addr=phone.accept()
    print(conn)
    print('client\'s ip and port ',client_addr)    

    p=multiprocessing.Process(target=service_client,args=(conn,))
    p.start()
    
    conn.close()


# close connection
conn.close()

# stop server

