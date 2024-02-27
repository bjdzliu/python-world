"""
****** 很少用 *****
send()给yield传值

"""


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
print("in main",res0)

#
# #"value"传递给x; 获取yield的一个返回值；即遇到yield 2222 ，返回2222
# res1=g.send("value") 传值后，在函数里运行，直到yield 2222
res1=g.send("value")
#res1 是2222
print(res1)


"""
x = yield 1111

通过 send 把值给了x
send()得到的返回值是1111 
yield进入等待状态
当再次遇到yield时，返回 1111

"""

def consumer():
    r = ''
    while True:
        n = yield r  # 函数返回r的值      第一次到此中断,只返回r的值
        if not n:  # 取真；没有物品
            return  # 函数结束
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)