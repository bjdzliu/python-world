import threading
import logging

FORMAT="%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt="%Y-%m-%d-%H:%M:%S")

def add(x,y):
    logging.warning("{} {}".format(threading.enumerate(),x+y))
    logging.info("%s %s",x,y)
t=threading.Timer(1,add,args=(4,5,))
t.start()



