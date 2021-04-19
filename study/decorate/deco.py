import time



# #### deco template
# def index(x):
#     print("exec in index",x)
#
# def outter():
#     def wrapper(x):
#         print("in outter")
#         index(x)
#     return wrapper
#
# newindex=outter()
#
# newindex(1)
#
# #### 为满足outter适用于其他函数，设计出outter2
# def index2(x):
#     print("exec in index2",x)
#
# def outter2(func):
#     def wrapper(x):
#         print("in outter")
#         func(x)
#     return wrapper
#
# newindex2=outter2(index2)
#
# newindex2(1)

###


# 有参数装饰器请查看 parame-deco.py
def outer2(func): ##为什么套一层outer2；为什么只有一个参数-(语法糖)
    #wrapper模拟成func；
    """
    func的参数、返回值、属性，wrapper都得和func一样
    :param func:
    :return:
    """
    def wrapper(*args,**key):
        start=time.time()
        time.sleep(1)
        res=func(*args,**key)
        stop=time.time()
        print(stop-start)
        return res
    return(wrapper)


## 使用语法糖，省略了语句：index=outer2(index)；这里只能传一个参数
@outer2
def index(x,y,u,otherkey):
    print("x",x,"y",y)
    print("key is",otherkey)
    return "my value in func"

def home(x,y,u,otherkey):
    print("x",x,"y",y)
    print("key is",otherkey)
    return "my value in func"

# def wrapper(*args,**key):
#     start=time.time()
#     time.sleep(1)
#     #*args,**key放在实参， 将参数拆分
#     #index(111,222,222,otherkey="a")
#     index(*args,**key)
#     stop=time.time()
#     print(stop-start)

# wrapper(111,222,222,otherkey="a")

### 优化方案1

### 任意函数都可以用wrapper
# def outer(func):
#     def wrapper(*args,**key):
#         start=time.time()
#         time.sleep(1)
#         func(*args,**key)
#         stop=time.time()
#         print(stop-start)
#     return(wrapper)
#
#

#
# newindex=outer(index)
#
# ##返回None
# print(newindex("a","b","c",otherkey="d"))


### 优化方案2
### 函数index的返回，也能正常获得
### 另外，使用语法糖

#newindex=outer2(index)

#正常返回index的return


print(index("a","b","c",otherkey="d"))

#叠加多个装饰器的加载顺序
# @deco3
# @deco2 #index=deco2(deco1(index))
# @deco1 #index=deco1(index)
# def index():
#     pass


