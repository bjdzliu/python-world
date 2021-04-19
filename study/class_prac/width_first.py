
"""
菱形继承

"""

class G: # 在python2中，未继承object的类及其子类，都是经典类
    def test(self):
        print('from G')

class E(G):
    def test(self):
        print('from E')

class F(G):
    def test(self):
        print('from F')

class B(E):
    def test(self):
        print('from B')

class C(F):
    def test(self):
        print('from C')

class D(G):
    def test(self):
        print('from D')

class A(B,C,D):
    # def test(self):
    #     print('from A')
    pass

obj = A()
print(A.mro())
obj.test()


###python2
"""
# 如上图，查找顺序为:obj->A->B->E->G->C->F->D->object
# 可依次注释上述类中的方法test来进行验证,注意请在python2.x中进行测试
"""

