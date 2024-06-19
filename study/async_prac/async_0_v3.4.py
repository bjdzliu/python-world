import asyncio
@asyncio.coroutine                #这是个异步函数，其内有异步操作
def hello():                             #hello（）的类型是coroutine
    print("Hello world!")               
    # 异步调用asyncio.sleep(1),线程不等待拿到none就去作别的事情。
    # asyncio.sleep的类型是coroutine，线程中断。这里1s后，默认返回值none。
    r = yield from asyncio.sleep(1)                                            
    print("Hello again!")
 
loop = asyncio.get_event_loop()  # 获取EventLoop: 时间循环模型声明协程，然后将其加入到EventLoop中， 即可实现异步IO。
                                                  
# 执行coroutine
loop.run_until_complete(hello()) #将hello()放到loop中执行
print("Executing in main()!")
loop.close()