import threading
import time

count=1
def eat():
    while True:
        print("main_thread()    ----> ",threading.main_thread())
        print("main_thread() status  -----> ",threading.main_thread().is_alive())
        print("current_thread()    >>",threading.current_thread().ident)
        time.sleep(0.5)
        global count
        if(count==8):
            raise Exception("eating threat quit")
        print("welcome to here",threading.current_thread)
        count+=1

def watch():
    for _ in range(11):
        time.sleep(0.5)
        print("i'm watching the tv")

thread1=threading.Thread(target=eat,name="hungry")
thread1.start()

thread2=threading.Thread(target=watch,name="happy")
thread2.start()

print(threading.active_count())
print(threading.enumerate())


