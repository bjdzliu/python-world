import  socket
import threading
import logging
logging.basicConfig(level=logging.INFO)

class chatServer:
    def __init__(self,ip="127.0.0.1",port=8090) -> None:
        self.addr=(ip,port)
        self.sock=socket.socket()
        self.sock.bind(self.addr)
        self.event=threading.Event()

    def start(self):
        self.sock.listen()
        threading.Thread(target=self._accecpt,args=(self.sock,),name="accept").start()

    def stop(self):
        pass

    def _accecpt(self,sock):
        while True:
            conn,client=sock.accept()
            threading.Thread(target=self._recv,args=(conn,),name="recv").start()
            logging.info(threading.enumerate())
       
        
    def _recv(self,conn):
        while not self.event.is_set():
            data=conn.recv(1024)
            conn.send(data)

s=chatServer()
s.start()



