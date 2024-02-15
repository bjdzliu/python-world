import threading

X='abc'
ctx=threading.local()
ctx.x=123

print(ctx,type(ctx),ctx.x)

def work():
    print(X)
    print(ctx)
    ctx.x=567
    ## try without ctx.x=567
    print(ctx.x)
    print("happy")

threading.Thread(target=work).start()

############
local_school=threading.local()

def process_student():
    std=local_school.student 
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name  #两个线程的 local_school.student 互不影响
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()