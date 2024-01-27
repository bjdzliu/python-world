# coding:utf-8

"""
dir
"""
class Foo(object):
    price = 50
    list2=[1,2,3]
    def how_much_of_book(self, n):
        print("print self object ",self)
        return self.price * n
foo = Foo()
print(foo.how_much_of_book(8))

foo.list2=[1,3,4,5]
print("方法中的list2 不因对象的改变而改变",Foo.list2)

## dir 列出类的方法和属性
print(dir(foo))

# print("foo's dir")
# print(foo.__dir__())


class Foo2():   
     __ho="private var, can't be read  directly" 
     __xxx__="can be read by object."
     _yyy="_yyy  can be read by object"
     ## 对象无法读取
     def __python(self):
            print("I love Python.")
 
     def code(self):
            print("Which language do you like?")
            self.__python()

     def wrap(self):
             return self.__ho

obj=Foo2()
print(obj.__xxx__)
print(obj._yyy)
print(obj.wrap())