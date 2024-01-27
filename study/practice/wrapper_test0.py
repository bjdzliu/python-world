def log(func):
    def decorator():    
        print(' in decorator: %s():' % ( func.__name__))
        func()
    return decorator
 
@log
def now():
    print('2013-12-25')

now()
# 输出结果是decorator
print(now.__name__)

print("# 不使用注解的方式   ")
def now2():
    print("execute in now2")

# 不使用注解的方式    
log_now2 = log(now2)
log_now2()



print("##### 另一个例子 ###    ")
## 
def deco(func):
    def _deco():
        print("before myfunc() called.")
        ss=func()
        print("  after myfunc() called.")
        return ss
    return _deco                  
 
@deco
def myfunc():                   
    print(" myfunc() called.")
    return 'ok'
 
ret=myfunc()   
print(ret)    
myfunc()
