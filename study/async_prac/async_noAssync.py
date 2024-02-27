import asyncio
import requests

async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的工O请求，自动化切换到其他任务）
    print("开始下载：",url)

    loop=asyncio.get_event_loop()
    #requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    print("下载完成")
    #图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name,mode='wb')as file_object:
        file_object.write(response.content)

if __name__ == "__main__":
    url_list = [
    "https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar_chsEe12AxQ6A00H_AAFocMs8nzu621.jpg",
    "https://ww2.autoimg.cn/newsdfs/g30/M01/3c/E2/120x90_0_autohomecar_chcCSv2BBICAUntfAADjJFd6800429.jpg",
    "https://ww3.autoimg.cn/newsdfs/g26/M0B/3c/65/120x90_0_autohomecar_chcCP12BFCmA1083AAGq7vKOsGY193.jpg"
    ]

tasks = [ download_image(ur1) for ur1 in url_list]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
