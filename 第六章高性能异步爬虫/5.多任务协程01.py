import asyncio
import time


async def request(url):
    print('正在下载', url)
    # 在异步协程中，如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    # 当在asynio中遇到阻塞操作必须手动挂起
    await asyncio.sleep(2)
    print('下载完毕', url)

start = time.time()
urls = ['www.baidu.com',
        'www.sogou.com',
        'www.google.com'
        ]

# 任务列表：存放多个任务对象
stasks=[]
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装的wait中
loop.run_until_complete(asyncio.wait(stasks))

end = time.time()
print(end-start)