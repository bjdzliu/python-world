import threading
import time

class Counter():
    def __init__(self) -> None:
        self._val=0
        #属性名前面有两个下划线（例如 __attribute）表示这是一个私有属性
        self.__lock=threading.Lock()

    @property
    def value(self):
        with self.__lock:
            return self._val
        
    # 两个加锁、解锁的方式：
    # try...finall 和 with    
    def inc(self):
        try:
            self.__lock.acquire()
            self._val+=1
        finally:
            self.__lock.release()

    def dec(self):
        with self.__lock:
            self._val-=1

        
def run(c:Counter,count=100):
    for _ in range(count):
        for i in range(-50,50):
            if i<0:
                c.dec()
            else:
                c.inc()

#一个公共对象
c=Counter()

c1=10
c2=1000

#启动c1个线程，每个线程，都会用函数run，来使用公共对象c
for i in range(c1):
    threading.Thread(target=run,args=(c,c2,)).start()

# c1个线程，每个执行10000次
# 没有运行完成，就打印c.value, 可能的值有:
# 0  因为刚开始，
# -120 一个中间值
print(c.value)

# 改进的方式：主线程一直等所有线程都执行完，再打印value
# 主线程判断只剩一个活动线程时，计算完毕，c.value=0
# while True:
#     if threading.active_count()==1:
#         print(threading.enumerate())
#         print(c.value)
#         break
#     else:
#         print(threading.enumerate())