def log(text):
    def decorator(func):    #func是函数now(),闭包的特性
        def wrapper(*args, **kw):   #为了包装func
            print('%s %s():' % (text, func.__name__))    #在func()前,新执行一段代码
            return func(*args, **kw)   #执行之前的函数功能func()
        return wrapper    # now = decorator(now)   #返回了一个新的函数func()
    return decorator
 
@log('execute log : ')
def now():
    print('2013-12-25')
now()