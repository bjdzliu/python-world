
import threading
import time

"""
用全局变量，给线程用，但是各线程之间是隔离的
每个线程是不同的任务，x是局部变量
"""

a=threading.local()
def worker():
    a.x=0
    for i in range(100):
        time.sleep(0.0001)
        a.x+=1
    print(threading.current_thread(),a.x)

for i in range(10):
    threading.Thread(target=worker).start()

