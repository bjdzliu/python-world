# coding: utf-8
from multiprocessing import Pool
import os, time, random
 
def long_time_task(name):   #定义子进程的行为
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()   #开始时间戳
    time.sleep(random.random() * 3)  #子进程随机休眠时间
    end = time.time()    #结束时间戳
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  #进程池里有4个进程
    for i in range(10):   #10次循环，比如10项工作
        #参数（要调用的目标函数，传递给函数的参数tuple）
        p.apply_async(long_time_task, args=(i,))  
        # 每次循环，会用空闲出来的子进程，去执行任务。

    print('Waiting for all subprocesses done...')
    #关闭进程池，没有任务要执行了
    p.close()
    # 如果是进程池里的任务，main 进程不会等待这些进程。
    # 如果没有join，主进程执行完，马上退出了
    # 和multiprocess 、threading通常的对进程、线程的处理方式不太一样
    #必须在close后面
    p.join()
    print('All subprocesses done.')


    