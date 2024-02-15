from threading import Event,Thread
import  logging,time

logging.basicConfig(level=logging.INFO)

def do(event:Event,interval:int):
    while not event.wait(interval):
        logging.info('do sth')

e=Event()

Thread(target=do,args=(e,2)).start()

if not e.wait(7):
    print("aaa")
e.set()

