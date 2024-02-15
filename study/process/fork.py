import os
 
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:

"""
执行 os.fork ()会创建两个进程: 父进程和子进程。它在子进程中返回0，在父进程中返回子进程 id。
"""
pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

## 父子进程都会执行
for i in range(0, 10):
    print("Printing the value %d from the Process: %d"%(i, pid))