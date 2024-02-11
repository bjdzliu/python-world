from multiprocessing import Process

'''
在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，
在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。
因此如果将process()直接写在文件中就会无限递归创建子进程报错。
所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候  ，就不会递归运行了。

'''

import os,time
# def run_proc(name):
#     time.sleep(3)
#     print("sub process run %s   ----  %s"%(name,os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Print process %s'%os.getpid())
#     print('Child process will start.')
#     p=Process(target=run_proc,args=('test',))
#     p.start()  ###告诉操作系统 创建一个process
#     #p.join()  ## 主进程等待子进程运行后，再继续运行
#     print("in main")

# 第二种方法,以继承Process类的形式开启进程：
def f(name):
    print('hello',name)
    print('method2 i am sub process')

class myprocess(Process):
    def run(self):
        print("start in sunb process, will sleep 3s")
        time.sleep(3)
        print("sub process run %s   ----  %s" % ('in',os.getpid()))

def f2(x):
    print('子进程id ：',os.getpid(),'父进程id ：',os.getppid())
    return x*x


if __name__ == '__main__':
    ##实例化一个process对象
    print("#############method1")
    s=myprocess()
    s.start()
    print("in main")
    print("############# method2")
    p=Process(target=f,args=('bob',))
    p.start()
    time.sleep(1)
    print("method2 in main")
    print("############# method3")
    print('main process id',os.getpid())
    p_lst=[]
    for i in range(5):
        p=Process(target=f2,args=(i,))
        p.start()



