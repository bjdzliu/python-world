import time
import asyncio

#函数被定义成 coroutine object
async def washing1():
    time.sleep(1)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了

async def washing2():
    time.sleep(2)
    print('washer2 finished')

async def washing3():
    time.sleep(1)
    print('washer3 finished')


async def washing4():
    await asyncio.sleep(3)  # 第4台洗衣机,
    print('washer1 finished')  # 洗完了

async def washing5():
    await asyncio.sleep(3)
    print('washer2 finished')

async def washing6():
    await asyncio.sleep(3)
    print('washer3 finished')




if __name__ == '__main__':
    
    ### 执行一个协程对象
    start_time = time.time()
    coroutine_1 = washing1()  # 协程是一个对象，不能直接运行
    loop = asyncio.get_event_loop()  # 创建一个事件循环
    result = loop.run_until_complete(coroutine_1)
    end_time = time.time()
    print('总共耗时：{}'.format(end_time-start_time))

    sss=washing2()
    r=loop.run_until_complete(sss)
    

    ### 执行多个协程对象，一点时间没节约
    ### 因为washing1的 sleep 是阻塞的
    print("执行多个coroutine object")
    start_time = time.time()
    tasks = [
        washing1(),
        washing2(),
        washing3()
    ]
    # asyncio.wait() 参数是可迭代对象
    loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print('执行多个coroutine object 总共耗时：{}'.format(end_time-start_time))


    ### 执行多个协程对象，节约时间
    print("执行多个coroutine object")
    start_time = time.time()
    tasks = [
        #三个协程对象
        washing4(),
        washing5(),
        washing6()
    ]
    #

    loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print('执行多个coroutine object 总共耗时：{}'.format(end_time-start_time))

