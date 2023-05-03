from selenium import webdriver
from time import sleep

path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://world.taobao.com/')

# 标签定位
search_input = browser.find_element_by_id('mq')
# 标签交互
search_input.send_keys('iphone')

# 执行一组js程序
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
btn = browser.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
btn.click()

browser.get('https://www.google.com')
sleep(2)
browser.back()

browser.forward()
sleep(5)

browser.quit()