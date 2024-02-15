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
    p = Pool(4)  #设定同时跑4个子进程，默认是CPU的个数
    for i in range(5):   #5个进程
        p.apply_async(long_time_task, args=(i,))  
    print('Waiting for all subprocesses done...')

    
    p.close()
    
    p.join()

    print('All subprocesses done.')

