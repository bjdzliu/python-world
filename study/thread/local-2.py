import threading


# 全局变量
X='global_value=100'

# Create a thread-local storage space
ctx=threading.local()
ctx.x=123

print(ctx,type(ctx),ctx.x)

def work():
    print(ctx)
    ctx.x=567
    ## try without ctx.x=567
    print("in work(): ",ctx.x)
    print("happy")
    global X
    X='is changed in work()'
    print("in work(), global value: ",X)

threading.Thread(target=work).start()
print("after work() ,X is",X)

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


