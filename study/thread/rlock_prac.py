import threading
import logging
logging.basicConfig(level=logging.INFO)

def worker(lock):
    print("enter worker func")
    lock.acquire()
    print("get acquire() in worker()")
    # with lock:
    #     print(f"{threading.current_thread().name} acquired the lock")
    #     # 这里可以执行一些需要同步的操作

# 创建一个可重复锁对象
my_lock = threading.RLock()
my_lock.acquire()
my_lock.acquire()
logging.info("main thread has been acquired")

# 在Main线程里，必须release后，在其他线程里，my_lock才能被再次acquire
# 可重复锁，不能在其他线程里release()
my_lock.release()
my_lock.release()
logging.info("main thread must be released")


# 在不同的线程中使用同一个锁对象
thread1 = threading.Thread(target=worker, args=(my_lock,), name="Thread-1")

# 启动线程
thread1.start()

# 等待线程结束
thread1.join()
