import threading,time,logging

logging.basicConfig(level=logging.INFO)
cups=[]
lock=threading.Lock()

def worker(lock:threading.Lock,task=100):
    while True:
        lock.acquire()
        count=len(cups)
        logging.info(count)
        if count>=task:
            lock.release()
            break
        cups.append(1)
        lock.release()
        logging.info("{} make 1.".format(threading.current_thread().name))

for x in range(10):
    threading.Thread(target=worker,args=(lock,100)).start()