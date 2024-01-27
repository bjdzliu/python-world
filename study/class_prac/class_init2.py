class Foo:
    __N=0
    def __init__(self,y):
        ## 变形为self._Foo__x
        self.__x=y

    def __f1(self):
        print('__f1 run')

    def f2(self):
        self.__f1()

print(Foo.__dict__)

print("111111",Foo._Foo__N)

obj1=Foo(100)
obj2=Foo(200)

print(obj1._Foo__x)

##

print(obj2._Foo__x)

obj1.f2()


##变形只在类初始化时，才会发生一次。
#'__M': 100
Foo.__M=100
Foo.__dict__
print(Foo.__dict__)
