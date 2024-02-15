import time
import threading

"""
只要有non-daemon线程，主线程退出时，也不会杀掉所有daemon线程。
知道所有non-daemon全部结束，如果还有daemon线程，主线程退出，会结束所有daemon线程，退出。
"""
def foo(n):
    for i in range(n):
        print(1)
        time.sleep(1)

t1=threading.Thread(target=foo,args=(10,),daemon=True)
t1.start()

t2=threading.Thread(target=foo,args=(20,),daemon=False)
t2.start()

time.sleep(2)
print("Main Threading Exiting")