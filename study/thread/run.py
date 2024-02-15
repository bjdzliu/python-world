import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("run")
        super().run()
    def start(self):
        print('start')
        return super().start()
    
def worker(n=5):
    print(threading.current_thread())
    for _ in range(n):
        time.sleep(0.5)
        print("i am running",threading.current_thread())

    print("i am tired")

t=MyThread(target=worker,args=(5,))
t.start()



print("==========================开始执行run()")
t0=MyThread(target=worker)
## run方法目前在主线程中。它也可以在其他线程里。
## 它就是一个函数的调用
t0.run()



for x in range(1):
    print(x)

