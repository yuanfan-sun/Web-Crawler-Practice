import asyncio


'''
# 生成一个事件循环
loop = asyncio.get_event_loop()

# 将任务放到'任务列表'
loop.run_until_complete(任务)

协程函数：定义函数时候 async def函数名
协程对象：执行协程函数（）得到的协程对象

async def func():
    pass

result = func() # 执行协程函数创建协程对象，内部代码不会执行
# 如果要运行协程函数内部代码，必须要将协程对象交给事件循环来处理
asyncio.run(result)

3.3 await
await+可等待对象（协程对象;future;Task对象-->IO等待）
await就是等执行完之后再往下

3.4 Task对象
在事件循环中添加多个任务

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def main():
    print('main开始')

    task_list = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]

    print('main结束')

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


asyncio.run(main())
'''


# asyncio.future对象
# concurrent.feature.Future对象
'''
3.6异步迭代器

'''

