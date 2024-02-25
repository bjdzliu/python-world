import threading
import logging
import random
logging.basicConfig(level=logging.INFO,format="%(thread)d %(threadName)s %(message)s")

class Conn:
    def __init__(self,name):
        self.name=name

class Pool:
    def __init__(self,count=3):
        self.count=count
        self.sema=threading.Semaphore(count)

        self.pool=[Conn("conn-{}".format(i)) for i in range(count)]
        print(self.pool)
        
        logging.info("pool length is {}".format(len(self.pool)))

    def get_conn(self):
        # 从连接池取走一个
        self.sema.acquire()
        data=self.pool.pop()
        return data
    
    def return_conn(self,conn:Conn):
        #如果return_conn比get_conn提前执行：
        # 加锁 or
        # try finally append后再剪减掉 or
        # 将list改成字典，取走后，置位
        self.pool.append(conn)
        #和上句之间，有可能被其他线程中断
        self.sema.release()

pool=Pool(3)

def worker(pool:Pool):
    conn=pool.get_conn()
    logging.info("get_conn is {}".format(conn))
    # 模拟使用了一段时间
    threading.Event().wait(random.randint(1,4))
    pool.return_conn(conn)

for i in range(6):
    threading.Thread(target=worker,name="worker-{}".format(i),args=(pool,)).start()







