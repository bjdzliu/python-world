import threading
import random
import logging
logging.basicConfig(level=logging.INFO,format="%(thread)d %(threadName)s %(message)s")

class Dispatcher:
    def __init__(self,x):
        self.count=x
        self.data=0
        self.event=threading.Event()
        self.cond=threading.Condition()

    def produce(self):
        #循环n次，每次间隔1s，1s后，获取锁，去生产
        for count in range(self.count):
            data=random.randint(1,100)
        #生产者对共享资源，拿锁，才能生产，生产后通知
            with self.cond:
                self.data=data
                logging.info("produce {}".format(count))         
                self.cond.notify(2)
            self.event.wait(1)               

    def custom(self):
        while not self.event.is_set():
            #为防止：如果生产者先notify，消费者wait不到通知，wait将永远被等待通知。
            with self.cond:
                self.cond.wait()
                logging.info(self.data)

def consumer(shared_resource):
    shared_resource.custom()

def producer(shared_resource):
    shared_resource.produce()


shared_resource=Dispatcher(10)

for i in range(5):
    threading.Thread(target=shared_resource.custom,name="c-{}".format(i)).start()


p=threading.Thread(target=producer,args=(shared_resource,),name="producer-t2")


p.start()

p.join()

