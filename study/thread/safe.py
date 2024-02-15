import threading
import logging
logging.basicConfig(level=logging.INFO)

def worker():
    for x in range(100):
       
        """
        线程不安全会发生在：
        print("{} is running".format(threading.current_thread()))
        字符串会连在一起
        print有两步：先打印字符串；再换行
        print函数线程不安全
        """
        #不让print打印换行
        #print("{} is running,\n".format(threading.current_thread().name),end='')

        #使用loggin
        msg="{} is running".format(threading.current_thread())
        logging.info(msg)

for x in range(5):
    threading.Thread(target=worker,name="worker-{}".format(x)).start()

