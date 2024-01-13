def log(func):
    def decorator():    
        print('%s():' % ( func.__name__))
        func()
    return decorator
 
@log
def now():
    print('2013-12-25')

now()

