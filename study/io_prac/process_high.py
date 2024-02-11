import time
from multiprocessing import Process

def f(name):
    print('hellm',name)
    time.sleep(1)

if __name__=='__main__':
    for i in range(5):
        p=Process(target=f,args=('%s%s'%('bob',i),))
        p.start()
        p.join()
    print('父进程在执行')

