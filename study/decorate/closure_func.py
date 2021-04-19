# # def person(name, age, **kw):
# #     print('name:', name, 'age:', age, 'other:', kw)
# #
# # person("xiaowang",16,home="asd")
#
# # def func2(kw):
# #     print(kw)
# # kw={1:"a",2:"b"}
# # func2(kw)
# #
# #
# # def func1(**kargs):
# #     print(type(kargs))
# #     for k,v in kargs.items():
# #         print(k,v)
# #
# # func1(kargs=1,oo=2)
#
#
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs
#产生三个函数
f1, f2, f3 = count()

print(f1(),f2,f3)
# 内存里i已经变成3了。在外层调用时，执行了i*i, 三个值是9
#

"""
返回的函数并没有立刻执行，而是直到调用了f()才执行。 f()称为闭包
 fs.append(f) 这里的f不算执行。
把f变成一个执行函数，将结果保留下来，就可以输出 1 4 9
"""
def count():
    fs = []
    for j in range(1, 4):
            def f(j):
                def g():
                    return j*j
                return g
            fs.append(f(j))
    return fs

a,b,c=count()
print(a(),b(),c())

