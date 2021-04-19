"""
yield 在函数内
除了next
还有其他用法
给yield传值

原来函数是一次执行到尾。
现在用了yield，函数可以等待其他输入。

send()  close()
"""


def dog(name):
    print("start to eat")
    while True:
        # 注意这里的执行顺序
        # 将g.send("apple")中的apple传递给x;函数继续执行；执行print；while true；yield 111返回 11
        x=yield 111   #111在下次遇到yield时，返回111
        print("%s eat %s" %(name,x))

g=dog("alex")
#第一次传none，类似初始化，x不会得到None；yield 111返回111
res = g.send(None)   #g.send(None) 等同于 next(g)

print("yield would be 111",res)

res2 = g.send("apple")
print("yileld would be 111 ",res2)

g.send("peach")


"""
x=yield 1111
顺序：
先通过next或send 把值给了x
执行；
当再次遇到yield时，返回 yield 1111

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