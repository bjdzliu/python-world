"""
有参装饰器
背景：
outer
wrapper
都不能另外的参数。
但是需要传入参数
"""

#有参数 山炮1号；没有语法糖

## 装饰器函数
# def deco(func,db_type):  #一个普通函数作为参数，“file“作为另一个参数
#     def wrapper(*args,**keys):
#         if db_type=='file':
#             print("this is a file auth method")
#             func(*args,**keys)
#         elif db_type=='db':
#             print("this is db auth method")
#             func(*args,**keys)
#     return wrapper


# ##普通函数
# def index(*args,**keys):
#     print("这是普通函数")

# #调用装饰器函数，返回wrapper
# index=deco(index,"file")

# index()
# ####

# def home(*args,**keys):
#     print("exec in home")
# home=deco(home,"db")

# home()



# exit(0)


############### 装饰器
def auth(db_type):
    def deco(func):
        def wrapper(*args,**keys):
            if db_type=='file':
                print("this is a file auth method")
                func(*args,**keys)
            elif db_type=='db':
                print("this is db auth method")
                func(*args,**keys)
        return wrapper
    return deco


@auth("file")
def index(*args,**keys):
    print("exec in index")

index()

#以下三行可以用语法糖替代
# newdeco=auth(db_type="file")
# newindex=newdeco(index)
# newindex()

@auth("db")
def home(*args,**keys):
    print("exec in home")

home()


