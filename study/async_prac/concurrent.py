
import time
import asyncio
# concurrent.futures和awaitable 对象 future 不是一回事
# concurrent.futures 会创建线程池
import concurrent.futures

'''
asyncio 和 线程池的配合
场景：当某个模块不支持异步时，但是其他模块还在用async，为了两者配合

'''

def func1():
    #某个耗时操作
    time.sleep(2)
    return"sB"


async def main():
    loop=asyncio.get_running_loop()
    #1.Run in the default loop'sexecutor（默认ThreadpoolExecutor)
    #第一步：内部会先调用ThreadpoolExecutor的submit方法去线程池中申请一个线程去执行func1函数，并返 回一个concurrent.futures.Future对象
    #第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asycio.Future对象。
    #因为concurrent.futures.Future对象不支持await语法，所以需要包装为asycio.Future对象才能使用。
    fut=loop.run_in_executor(None,func1)
    result = await fut
    print('default thread pooi',result)

    # 2.Runin a custom threadpool:
    # with concurrent.futures.ThreadpoolExecutor() as pool:
    #   result= awaitloop.run_in_executor(
    #       pool,func1)
    #   print('customthreadpooi',result)


    # 3.Run in a custom process pool:
    #with concurrent.futures.ProcessPoolExecutor()aspool:
    #  result=awaitloop.run_in_executor(
    #    pool, func1)
    #  print('custom process pooi',result)


asyncio.run(main())
