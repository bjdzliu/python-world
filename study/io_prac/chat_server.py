from socket import *
from multiprocessing import Process


#AF_INET 基于网络通信
#SOCK_STREAM 流式协议


def talk(conn,client_addr):
    while True:
        try:
            msg = conn.recv(1024)
            # 在unix下，data收到空，意味这异常行为：client非法断开连接
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            # 异常处理，针对windows系统；windows不显示data为0
            break

if __name__=='__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8087))
    server.listen(5)

    while True:
        conn,client_addr=server.accept()
        print(client_addr)
        p=Process(target=talk,args=(conn,client_addr,))
        p.start()

