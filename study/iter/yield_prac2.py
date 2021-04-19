def func():
    print("start")
    x=yield 111
    print("x' value is",x)
    # print("after first yield")
    # print("after first yield")
    # print("after first yield")
    # print("after first yield")
    # print("after first yield")
    yield 2222

g=func()
#首次初始化
res0=g.send(None)
# #代码暂停在yield 111
print("1",res0)

#
# #"value"传递给x; 获取yield的一个返回值；即遇到yield 2222 ，返回2222
# res1=g.send("value") 传值后，在函数里运行，直到yield 2222
res1=g.send("value")
#res1 是2222
print(res1)