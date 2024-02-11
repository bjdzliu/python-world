#!/usr/bin/python
# -*- coding: UTF-8 -*-


class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法
        return cls()

    @staticmethod  #将函数装饰盛一个静态方法
    def func3():
        print('staitc')


obj=A.func2()  # 不需要实例化
print(obj.bar)

#static 类可以调用func3()； 只有绑定方法才有传参的效果
A.func3()
print("obj.func3():")
obj.func3()

#static
print("static::")
obj.func3()

print("静态、非绑定",A.func3)
print("类方法，绑定给对象",A.func2)
print("绑定给对象，调用者是对象",obj.func1)

print(obj.__class__)
print(A.__module__)