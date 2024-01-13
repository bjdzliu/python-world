import time
def calculate_time(f):
    def inner(*args,**kwargs):
        start_time=time.time()
        ret=f(*args,**kwargs)
        end_time=time.time()
        print(end_time-start_time)
        return ret
    return inner

@calculate_time
def add(m,n):
    time.sleep(2.2)
    return m+n

print(add(1,2))







