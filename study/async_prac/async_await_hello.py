
import  asyncio


async def main():
    print('hello')
    # await 后面要是一个等待对象（协程对象，Future，Task对象（IO等待））
    # 可等待 对象有三种主要类型: 协程, 任务 和 Future .
    await asyncio.sleep(3)
    print('world')

asyncio.run(main())

print("end")

