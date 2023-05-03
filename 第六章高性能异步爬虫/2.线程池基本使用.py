import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool
if __name__ == '__main__':
    start_time = time.time()


    # 使用线程池方式执行
    def get_page(str):
        print("正在下载：", str)
        time.sleep(2)
        print("下载完成：", str)


    name_list = ['aa', 'bb', 'cc', 'dd']

    # 实例化一个线程池对象
    pool = Pool(4)
    # 将列表中每一个列表元素传递给get_page进行处理
    pool.map(get_page, name_list)

    # for i in range(len(name_list)):
    #     get_page(name_list[i])

    end_time = time.time()
    print(f'用时{end_time - start_time}秒')