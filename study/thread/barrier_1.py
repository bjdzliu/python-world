import threading
import logging
logging.basicConfig(level=logging.INFO,format="%(thread)d %(threadName)s %(message)s")

def worker(barrier:threading.Barrier):
    ##每三个线程，在barrier前等待。
    logging.info("n_waiting={}".format(barrier.n_waiting))
    try:
        #达到参与方数量时，被唤醒
        #返回所有barrier后面的index
        bid=barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broker barrier in {}".format(threading.current_thread().name))

barrier =threading.Barrier(3)
event=threading.Event()

for x in range(5):
    event.wait(1)
    threading.Thread(target=worker,args=(barrier,)).start()