#导入webdriver
from selenium import webdriver
import time
import re

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
driver.set_window_size(1920, 900)
#如果没有在环境变量指定PhantomJS位置
driver = webdriver.PhantomJS(executable_path = "./phantomjs")

#get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)
driver.get("https://www.autohome.com.cn/car/")
time.sleep(2)

#需要点击a-z的按钮后，才可以把所有的数据拿到
# driver.find_element_by_class_name('find-letter-list')
# list = driver.find_elements_by_css_selector('.find-letter-list li a')
# print(list)
# for i in list:
#   print(i.val())
jsStr = 'var a = document.querySelector(".find-letter-list li a[data-meto=E]").click()'
driver.execute_script(jsStr)
time.sleep(2)
res = driver.find_elements_by_css_selector('#htmlE dl')
print(res)
