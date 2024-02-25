import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    # 不是 concurrent 的
    await say_after(1,'hello')
    await say_after(3,'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())