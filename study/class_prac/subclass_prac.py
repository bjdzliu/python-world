"""
单继承
利用双下划线，指定执行 父类 的方法
b.f2() 执行的是父类中的__f1

虽然子类也有__f1，但是和父类，各玩各的

"""

class Foo:
    def __init__(self):
        print("Foo __init__ is executed")
    def __f1(self):
        print('Foo.f1')
    def f2(self):
        print('Foo.f2')
        self.__f1()


class Bar(Foo):
    def __f1(self):
        print('Bar.f1')

    def get_f1(self):
        self.__f1()

    def f2(self):
        print("execute in Bar")
     
b=Bar()
b.f2()
b.get_f1()



# Foo.f2
# Foo.f1
# Bar.f1


