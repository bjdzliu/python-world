class E:
    def test(self):
        print('from E')

class F:
    def test(self):
        print('from F')

class B(E):
    def test(self):
        print('from B')

class C(F):
    def test(self):
        print('from C')
class D:
    def test(self):
        print('from D')
class A(B, C, D):
    # def test(self):
    #     print('from A')
    pass

print(A.mro())
'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.D'>, <class 'object'>]
'''
obj = A()
obj.test() # 结果为：from B
# 可依次注释上述类中的方法test来进行验证