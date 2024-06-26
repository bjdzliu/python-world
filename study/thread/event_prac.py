from threading import Event,Thread

import logging,datetime

logging.basicConfig(level=logging.INFO)

def add(x:int,y:int):
    logging.info(x+y)


## 通过共享事件，协调线程。
class Timer():
    def __init__(self,interval,fn,*args,**kwargs) -> None:
        self.interval=interval
        self.fn=fn
        self.args=args
        self.kwargs=kwargs
        self.event=Event()
    def start(self):
        Thread(target=self.__run).start()

    #    
    def cancel(self):
        self.event.set()
    
    def __run(self):
        start=datetime.datetime.now()
        logging.info("waiting")
        #等待x秒，超时后flag是false
        self.event.wait(self.interval)

        if not self.event.is_set():
            #fn是add函数, *self.args 解tuple pack。
            self.fn(*self.args,**self.kwargs)
        delta=(datetime.datetime.now()-start).total_seconds()
        logging.info('finished{}'.format(delta))

#先等待10s
#执行add 4+50
t=Timer(10,add,4,50)
t.start()


# e=Event()
# e.wait(4)



        




