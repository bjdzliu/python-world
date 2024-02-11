import time,os
from multiprocessing import Process



def run_proc(name,n):
    time.sleep(n)
    print("sub process run %s   ----  %s"%(name,os.getpid()))



# if __name__ == '__main__':
#     start_time=time.time()
#     ##实例化一个process对象
#     s = Process(target=run_proc,args=('s',1))
#     s2 = Process(target=run_proc,args=('s2',2))
#     s3 = Process(target=run_proc,args=('s3',3))
#     s.start()
#     s2.start()
#     s3.start()
#     s.join()
#     s2.join()
#     s3.join()
#     print("in main",time.time()-start_time)


if __name__ == '__main__':
    proc_list=[]
    start_time=time.time()
    ##实例化一个process对象
    for n in range(1,4):
        s = Process(target=run_proc, args=('s', n))
        s.start()
        proc_list.append(s)
        #join放在这里，等待第一个prcess，在等待第二个process，导致串行了
        #p.join()
    for p in proc_list:
        p.join()

    print("in main",time.time()-start_time)
