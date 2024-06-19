import asyncio
import time

'''
包含：
协程函数的嵌套
一个协程函数里，可以有多个await
'''

# 工作任务2
async def add_clothes():
    print('往洗衣机添加衣服....')
    await asyncio.sleep(4)       # 模拟这个任务耗时2秒

# 工作任务1， 其中执行工作任务2
async def washing1():
    print('洗衣机工作之前，需加衣服进去')
    await add_clothes()  # 等待这个事情完成,等add_clothes()执行结束，才能继续执行
    print('衣服加进去，可以开始工作了。。。。')
    await asyncio.sleep(3)  # 模拟洗衣机工作的耗时
    print('washer1 finished')  # 洗完了

# 增加一个洗衣机2
async def washing2():
    print('洗衣机2工作之前，需加衣服进去')
    await add_clothes()  # 等待这个事情完成
    print('洗衣机2衣服加进去，可以开始工作了。。。。')
    await asyncio.sleep(2)  # 模拟洗衣机工作的耗时
    print('washer1 finished')  # 洗完了

#
#asyncio.get_event_loop() 用于获取当前的事件循环。如果当前线程还没有事件循环，这个函数会抛出一个错误

start_time = time.time()
coroutine_1 = washing1() # 协程是一个对象，不能直接运行
coroutine_2 = washing2() # 协程是一个对象，不能直接运行
loop = asyncio.get_event_loop()  # 创建一个事件循环
result = loop.run_until_complete(asyncio.wait([coroutine_1,coroutine_2]))  # 将协程对象加入到事件循环中，并执行
end_time = time.time()
print('-----------end washing----------')
print('总共耗时:{}'.format(end_time-start_time))


### 模拟了两个洗衣机，执行时间是 max(washing1,washing2)
### 在主函数，执行 asyncio.run(main()): 为什么会影响运行 . loop混乱了。建议只执行一个loop 或者 asyncio.run()



