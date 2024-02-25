import asyncio

async def task2():
    print('task2:hello')
    # await 后面要是一个等待对象（协程对象，Future，Task对象（IO等待））
    # 可等待 对象有三种主要类型: 协程, 任务 和 Future .
    await asyncio.sleep(3)
    print('task2:world')



# 如果想在等待main()的时候，执行其他工作，需要再定一个异步函数
async def additional_task():
    print("Additional task: Start")
    await asyncio.sleep(2)
    print("Additional task: End")


async def main():
    tasks = [
        additional_task(),
        task2()
    ]
    task_objects = [asyncio.create_task(task) for task in tasks]

    #Running Tasks Concurrently
    await asyncio.gather(*task_objects)


asyncio.run(main())

# 执行 main()后，才能执行print
print("start do other things....")
print("start do other things....")

