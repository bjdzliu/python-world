#all
#可迭代对象，中每一个值都返回做bool运算，都为true，返回true
print(all([1,3,'']))
print(all([1,3,4]))
print(all([]))

#'' 空值的bool返回false
print(bool(''))

#有任意为真，则返回真
print(any([1,3,None]))

print(bin(11))
#
print(bin(11))
print(oct(11))

#判断是否可以别调用
class Foo():
    initvalue=100
    def test(self):
        print("t")
a=10
print(callable(a))
print(callable(Foo))
print(dir(Foo))

#反射相关的
#setattr
#getattr

#用isinstance做类型判断 type()不推荐使用
obj1=Foo()
print(isinstance(obj1,Foo))


#!/usr/bin/env python
# coding=utf-8
from math import sqrt

#python3 可迭代
#python2 直接返回list
res=range(2, 10, 2)
for x in res:
    print("range in python3 ",x)



## 2 起点；6终点；1 步长
## sqrt 取平方根
for n in range(2, 6, 1):
    # root=2.0  n=4
    root = sqrt(n)
    # 这里利用的int和float可以互相比较  duck类型。但是float和其他类型比较就不行
    if root == int(root):
        print(n)
        break
    else:
     print("Nothing.")

print(divmod(1000,33))

print(sorted([36, 5, 12, 9, 21]))