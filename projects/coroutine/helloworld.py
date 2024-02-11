# -*- coding: utf-8 -*-
import asyncio
import threading
@asyncio.coroutine
def hello(index,defaultarg="123"):
    """
    获取一个连接
    """
    print('arg is %s' %defaultarg)
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread()))
    yield from asyncio.sleep(5)
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread()))


loop = asyncio.get_event_loop()
print(type(loop))
tasks = [hello(1,"111"), hello(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


def writer():
    # 读取send传进的数据，并模拟写进套接字或文件
    while True:
        w = (yield)    # w接收send传进的数据
        print('>> ', w)

def writer_wrapper(coro):
    coro.send(None)
    while True:
        try:
            x=(yield )
            coro.send(x)
        except StopIteration:
            pass

w=writer_wrapper(writer())
w.send(None)
w.send(1)

