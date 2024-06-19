import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)
    return f"{what} - {delay}"

#这个是串行的
async def main():
    print(f"started at {time.strftime('%X')}")
    # 不是 concurrent 的！！！！！
    # 等say_after(3,'hello')执行完，才能执行say_after(6,'hello')
    # 创建一个task，将say_after(3,'hello')加入到事件循环中，并执行
    # await 一个coroutine对象
    await say_after(3,'hello')
    print(" say_after(3,'hello') is end")
    await say_after(2,'world')
    print(f"main finished at {time.strftime('%X')}")

#这个是并发的
async def main2():
    print(f" main2 started at {time.strftime('%X')}")
    # 创建一个task，将say_after(3,'hello')加入到事件循环中，并执行
    task1 = asyncio.create_task(say_after(3,'hello'))
    task2 = asyncio.create_task(say_after(4,'world'))
    #拿返回值
    # await等待task1执行完，获取返回值
    ret1=await task1
    ret2=await task2
    
    #获取全部的返回值
    results=await asyncio.gather(task1,task2)

    ret=await asyncio.gather(
        #gather也支持传入多个参数，参数是coroutine对象，gater自动将coroutine对象包装成task对象
        say_after(3,'hello'),
        say_after(2,'world')
    )

    print("main2结束")
    print(f"finished at {time.strftime('%X')}")


#asyncio.run 3.7引入的新函数，用来运行最高层级的入口点
#在 asyncio 内部，它创建一个新的事件循环，并在该循环上运行传入的协程。
asyncio.run(main2())

#创建一个事件循环，将main() task加入到事件循环中，并执行    
asyncio.run(main())