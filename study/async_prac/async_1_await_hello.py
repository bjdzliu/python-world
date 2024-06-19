
import  asyncio

async def calcu():
    print("start calculating")
    await asyncio.sleep(1)
    print("end calculating")
     

async def main():
    print('hello')
    # await 后面要是一个等待对象（协程对象，Future，Task对象（IO等待））
    # 可等待 对象有三种主要类型: 协程, 任务 和 Future .
    await asyncio.sleep(3)
    print('world')


## 3.7之前，asyncio.ensure_future
## 3.7之后，可以用asyncio.create_task()
tasks=[
        asyncio.ensure_future(calcu()),
        asyncio.ensure_future(main())
]

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

#asyncio.run(main())

print("end")

