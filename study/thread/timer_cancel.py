
import threading,time

def add(**kwargs):
    for k,v in kwargs.items():
        print(k)
values={"a":1,"c":2}       
t=threading.Timer(3,add,kwargs=values).start()


t2=threading.Timer(6,add,kwargs=values)
t2.cancel() #提前取消，也可以放在t2.start()后面
t2.start()


time.sleep(5)