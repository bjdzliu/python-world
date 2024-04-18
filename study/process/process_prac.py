

from multiprocessing import Process
import os
print("process will do this again")
def run_proc(name):
    print("run %s   ----  %s"%(name,os.getpid()))

if __name__ == '__main__':
    print('Print process %s'%os.getpid())
    print('Child process will start.')
    p=Process(target=run_proc,args=('worker process',))
    p.start()
    p.join()
 