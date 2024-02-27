import time
import asyncio

async def washing1():

    #这里time.sleep 因为是阻塞的，所以是三个washing顺序执行
    #time.sleep(3)  # 第一台洗衣机,

    await asyncio.sleep(2)  
    print('washer1 finished')  # 洗完了

async def washing2():
    #time.sleep(8)
    await asyncio.sleep(3)  
    print('washer2 finished')

async def washing3():
    #time.sleep(5)
    await asyncio.sleep(4)  
    print('washer3 finished')


async def main():
    print('start main:')
    start_time = time.time()

    #create_task return task
    #参数是 coroutine
    #将washing1()添加到事件循环
    task1 = asyncio.create_task(washing1())
     #将washing2()添加到事件循环
    task2 = asyncio.create_task(washing2())
    task3 = asyncio.create_task(washing3())

    print("main结束")

    ##事件循环中，有main 、三个washing task

    #因为在事件循环中，并且遇到await时， 协程将切换

    #main等待task1-3结束,如果注释掉await，main直接结束，打印不出task1-3的内容
    await task1
    # 因为task1执行时间最短，task1先执行完毕，main等task1执行完毕后，继续等task2 task3
    # 在await之前，task加入到事件循环时，已经开始执行了
    print("task1 end")
    await task2
    await task3

    end_time = time.time()
    print('-----------end main----------')
    print('总共耗时:{}'.format(end_time-start_time))

if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()  # 创建一个事件循环
    result = loop.run_until_complete(main())  # 将协程对象加入到事件循环中，并执行
