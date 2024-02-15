import threading
import logging
logging.basicConfig(level=logging.INFO)


def worker():
    for x in range(100):        
        msg="{}-{} is running!!".format(threading.current_thread(),x)
        logging.info(msg)


"""
线程daemon为true时，主线程不等待其结束，主线程结束
daemon值默认继承自当前线程
主线程daemon=false,所以不指定daemon时，线程是non-daemon

"""
threading.Thread(target=worker,daemon=True).start()
# 无法保证ending的输出位置，可能在线程输出前，也可能在线程输出后
print("ending")
print(threading.enumerate())


