# coding:utf-8

import time,threading

balance=0
lock=threading.Lock()


def change_it(n):
    global balance
    global lock
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for _ in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))

t2=threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()

#等t1 t2都执行ok
t1.join()
t2.join()

print(balance)



