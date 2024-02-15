# coding:utf-8
import time,threading

def loop():
    print('thread %s is running ..'% threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s end' % threading.current_thread().name)


print(' thread name  %s run' % threading.current_thread().name)

t=threading.Thread(target=loop,name="LoopThread")
t.start()

#主进程等待t
t.join()

for i in range(4):
    print("main thread is doing %s apple" % i)





