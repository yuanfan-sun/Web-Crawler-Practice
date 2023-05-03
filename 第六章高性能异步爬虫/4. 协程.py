import asyncio

async def request(url):
    print('正在请求的url是', url)
    print('请求成功', url)
    return url

# async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')
# asyncio.run(c)

# task的使用
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callback_func(task):
    # result返回的是任务对象中封装的协程对象的返回值
    print(task.result())

# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
