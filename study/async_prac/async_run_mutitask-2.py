import time
import asyncio

#函数被定义成 coroutine object

async def washing4():
    await asyncio.sleep(3)  # 第4台洗衣机,
    print('washer4 finished')  # 洗完了

async def washing5():
    await asyncio.sleep(3)
    print('washer5 finished')

async def washing6():
    await asyncio.sleep(3)
    print('washer6 finished')


async def washing7():
    await asyncio.sleep(3)
    print('washe7 finished')

if __name__ == '__main__':
    ### 执行多个协程对象，节约时间
    print("执行多个coroutine object")
    start_time = time.time()
    tasks = [
        #三个协程对象
        washing4(),
        washing5(),
        washing6(),

        # 错误：no running event loop 因为这时还没有事件循环
        #asyncio.create_task(washing7(),name="new task")
    ]
    ## 这里内部自动将 tasks 添加到事件循环了
    done,pending=asyncio.run(asyncio.wait(tasks))
    end_time = time.time()
    print('执行多个coroutine object 总共耗时：{}'.format(end_time-start_time))

