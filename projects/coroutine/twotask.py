import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()   #得到一个标准的事件循环,事件循环则被用来安排协同程序的执行
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks)) #asyncio.wait，通过它可以获取一个协同程序的列表，同时返回一个将它们全包括在内的单独的协同程序
loop.close()
