import asyncio
import requests

async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的工O请求，自动化切换到其他任务）
    print("开始下载：",url)

    loop=asyncio.get_event_loop()
    #requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    #run_in_executor这个函数将阻塞的IO操作委托给一个另外的线程或进程执行，这样事件循环就可以继续处理其他非阻塞的操作。
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    print("下载完成")
    #图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name,mode='wb')as file_object:
        file_object.write(response.content)

if __name__ == "__main__":
#     url_list = [
#     "https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar_chsEe12AxQ6A00H_AAFocMs8nzu621.jpg",
#     "https://ww2.autoimg.cn/newsdfs/g30/M01/3c/E2/120x90_0_autohomecar_chcCSv2BBICAUntfAADjJFd6800429.jpg",
#     "https://ww3.autoimg.cn/newsdfs/g26/M0B/3c/65/120x90_0_autohomecar_chcCP12BFCmA1083AAGq7vKOsGY193.jpg"
#     ]

# tasks = [ download_image(ur1) for ur1 in url_list]
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

        def blocking_io():
            # File operations (such as logging) can block the
            # event loop: run them in a thread pool.
            with open('/dev/urandom', 'rb') as f:
                return f.read(100)


        import asyncio
        import time
        import requests

        def blocking_io():
            print('start blocking_io')
            time.sleep(3)
            print('finish blocking_io')
        def blocking_io2():
            print('start blocking_io2')
            time.sleep(3)
            print('finish blocking_io2')

        async def main():
            #该函数返回当前正在执行的事件循环。
            loop = asyncio.get_running_loop()
            # result = await loop.run_in_executor(
            #         None, blocking_io)
            # result2 = await loop.run_in_executor(
            #         None, blocking_io2)
            result, result2 = await asyncio.gather(
             loop.run_in_executor(None, blocking_io), 
             loop.run_in_executor(None, blocking_io2))
            print('default thread pool', result)
            print('default thread pool', result2)

        asyncio.run(main())