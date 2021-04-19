# coding:utf-8

"""
类的初始化

dict
dir

"""
class Foo(object):
    price = 50
    list2=[1,2,3]
    def how_much_of_book(self, n):
        print(self)
        return self.price * n
foo = Foo()
print(foo.how_much_of_book(8))


foo.list2=[1,3,4,5]

print(Foo.list2)

## dir 列出方法和属性
#print(dir(foo))
print("foo's dir",foo.__dir__())

# '__dict__'
#以dict的形式，__dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值。
print(Foo.__dict__)


class Spring(object):
    season = "the spring of class"
s = Spring()
#对象的dict是空的
print(s.__dict__)

#类的dict
print(Spring.__dict__)

print(s.season)

s.season = "the spring of instance"
print(s.__dict__)

#对象内部，添加属性
s.lang="python"

print(s.__dict__)

#类添加属性，对象中没有。查找顺序：先在对象中找，再去类中找
Spring.flower = "peach"
Spring.__dict__['flower']

print(s.__dict__)