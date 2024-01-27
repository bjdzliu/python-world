class A(object):
    bar = "inner parameter"

    def func1(self):
        print('func1 is executed')


    @classmethod
    def func2(cls):
        print('func2 is executed')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法
        return cls()

    @staticmethod  #将函数装饰盛一个静态方法
    def func3():
        print('staitc')


obj=A()
obj.func1()
obj.func3()