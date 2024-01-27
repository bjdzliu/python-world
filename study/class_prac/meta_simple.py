class M(type):
    def __new__(cls,name,bases,dict):
        print("implictly invoke in M")
        print(name,bases,dict)
        return type.__new__(cls,name,bases,dict )
    
    ## init 函数,在定义 class A 时 ,被调用
    def __init__(self,name,bases,dict):
        print(name,bases,dict)
        return type.__init__(self,name,bases,dict)

    # 在A() 时,被调用
    def __call__(cls,*args,**kwargs):
        print("call")
        return type.__call__(cls,*args,**kwargs)

class A(metaclass=M):
    pass

o=A()
