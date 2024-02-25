import threading
import random
import logging
logging.basicConfig(level=logging.INFO)

class Dispatcher:
    def __init__(self,x):
        #count表示produce的次数
        self.count=x
        #data是生产的变量
        self.data=0
        self.event=threading.Event()
        self.cond=threading.Condition()

    def produce(self):
        #循环n次，每次间隔1s，1s后，获取锁，去生产
        for count in range(self.count):
        #生产者对共享资源，拿锁，才能生产，生产后通知
            with self.cond:
                self.data=random.randint(1,100)     
                logging.info("produce {}".format(count))         
                self.cond.notify_all()      
            self.event.wait(1)
                

    def custom(self):
        while not self.event.is_set():
            #为防止：如果生产者先notify，消费者wait不到通知，wait将永远被等待通知。
            with self.cond:
                self.cond.wait()
                logging.info("{} and thread is {}".format(self.data,threading.current_thread().name))

def consumer(shared_resource):
    shared_resource.custom()

def producer(shared_resource):
    shared_resource.produce()


shared_resource=Dispatcher(10)

c1=threading.Thread(target=consumer,args=(shared_resource,),name="consumer-t2")
c2=threading.Thread(target=consumer,args=(shared_resource,),name="consumer-t3")
p=threading.Thread(target=producer,args=(shared_resource,),name="producer-t2")


c1.start()
c2.start()
p.start()


c1.join()
c2.join()
p.join()

