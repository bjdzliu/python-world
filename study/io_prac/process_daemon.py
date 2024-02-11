import os
import time

from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person=person

    def run(self):
        print(os.getpid(),self.name)

        print('%s doing'%self.person)

if __name__ == '__main__':
    p=Myprocess('哪吒')
    p.daemon=True
    p.start()
    time.sleep(19)
    print("main")


#
# import time
# from multiprocessing import Process
#
# def func():
#     print('子进程 start')
#     time.sleep(3)  # 睡3秒的时候主进程的代码已经执行完毕了，所以子进程也会跟着结束
#     print('子进程end')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True  # daemon是Process的属性
#     p.start()
#     time.sleep(2)  # 睡2秒的时候，执行了子进程
#     print('主进程')