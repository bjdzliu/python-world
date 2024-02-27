import asyncio


async def task2():
    print('task2:hello')
    # await 后面要是一个等待对象（协程对象，Future，Task对象（IO等待））
    # 可等待 对象有三种主要类型: 协程, 任务 和 Future .
    await asyncio.sleep(3)
    print('task2:world')
    return "task2"



# 如果想在等待main()的时候，执行其他工作，需要再定一个异步函数
async def additional_task():
    print("Additional task: Start")
    await asyncio.sleep(2)
    print("Additional task: End")
    return "additional_task"


async def main():
    tasks = [
        additional_task(),
        task2()
    ]
    #将tasks添加到已有的事件循环中
    #事件循环：asyncio.run(main()) 这里创建的
    task_objects = [asyncio.create_task(task) for task in tasks]

    #Running Tasks Concurrently
    #await asyncio.gather(*task_objects)

    
    done,pending= await asyncio.wait(task_objects)
    #打印集合
    print(done)


### 注意⚠️：这里已经有事件循环了
asyncio.run(main())


# 执行 main()后，才能执行print
print("start do other things....")
print("start do other things....")

