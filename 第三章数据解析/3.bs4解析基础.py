from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 将本地的html文档中的数据加载到该对象中,参数1为fp 'r'=read
    fp = open('./test.html', 'r', encoding='utf-8')
    Soup = BeautifulSoup(fp, 'lmxl')
    print(Soup)
