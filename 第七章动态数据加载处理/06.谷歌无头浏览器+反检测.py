from selenium import webdriver
from time import sleep
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 规避检测
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 如何实现让selenium规避被检测到的风险
path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options, options=option)

# 无可视化界面(无头浏览器) phantomJs
browser.get('https://world.taobao.com/')

print(browser.page_source)
sleep(2)
browser.quit()
