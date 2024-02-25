import asyncio,time

async def nested():
    print("nested is invoke")
    await asyncio.sleep(0.5)
    print("nested is invoke")
    print("nested is invoke")
    await asyncio.sleep(0.5)
    print("nested is invoke")
    print("nested is invoke")
    return 42

async def task2_nested():   
    print("task2_nested is invoke")
    await asyncio.sleep(0.5)
    print("task2_nested is invoke")
    return 88


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    task_2 = asyncio.create_task(task2_nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    result = await task
    result2 = await task_2
    return result,result2

result1,result2=asyncio.run(main())

print(result1,result2)