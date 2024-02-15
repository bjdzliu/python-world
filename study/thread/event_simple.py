from threading import Event,Thread
import logging
import time

FORMAT= '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

def boss(event:Event):
    
    logging.info("im boss,waiting for worker cups")
    event.wait()
    logging.info("good")

def worker(event:Event,count=10):
    logging.info("im working")
    cups=[]
    while True:
        logging.info('make 1')
        time.sleep(0.5)
        cups.append(1)
        if len(cups) >= count:
            event.set()
            break
    logging.info("done cups={}".format(cups))

event=Event()
event2=Event()
print(id(event)==id(event2))

w=Thread(target=worker,args=(event,))
b=Thread(target=boss,args=(event,))

w.start()
b.start()


