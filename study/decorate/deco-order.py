"""


"""
def deco1(func1): # func1 = wrapper2的内存地址
    def wrapper1(*args,**kwargs):
        print('正在运行1===>deco1.wrapper1')
        res1=func1(*args,**kwargs)
        print('正在运行7===>deco1.wrapper1')
        return res1
    return wrapper1

def deco2(func2): # func2 = wrapper3的内存地址
    def wrapper2(*args,**kwargs):
        print('正在运行2===>deco2.wrapper2')
        res2=func2(*args,**kwargs)
        print('正在运行6===>deco2.wrapper2')
        return res2
    return wrapper2

def deco3(x):
    def outter3(func3): # func3=被装饰对象index函数的内存地址
        def wrapper3(*args,**kwargs):
            print('正在运行3===>deco3.outter3.wrapper3')
            res3=func3(*args,**kwargs)
            print('正在运行5===>deco3.outter3.wrapper3')
            return res3
        return wrapper3
    return outter3


# 加载顺序自下而上(了解)
@deco1      # index=deco1(wrapper2的内存地址)        ===> index=wrapper1的内存地址
@deco2      # index=deco2(wrapper3的内存地址)        ===> index=wrapper2的内存地址
@deco3(111) # ===>@outter3===> index=outter3(index) ===> index=wrapper3的内存地址
def index(x,y):
    print('正在运行4===>index')
    print('from index %s:%s' %(x,y))

index(1,2) # wrapper1(1,2)
