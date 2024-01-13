# def f_g():
#     a=1
#     yield a
#     a=2
#     yield a
#     a=3
#     yield a

# print(f_g())

# g=f_g()
# print(g.__next__())
# print(g.__next__())
# print(next(g))

##############################################################
# def data():
#     for i in range(1,1000):
#         yield i
# d=data()
# for i in range(1,10):
#     print(next(d))

# print("-------------")
# for i in range(1,10):
#     print(next(d))


######### send 方法 给上一个yield传递数值
def f():
    a=yield 2
    print("a=",a)

    b=yield a
    print("b=",b)

    c=yield b


g=f()
print(g.__next__()) 

#ahahah 被传递给 a=yield 2 中的 a
print(g.send("ahahah"))

print(g.send("22222"))



