import win32com.client
from selenium import webdriver
import time
brower=webdriver.Chrome()
brower.get('https://tinypng.com/')
brower.implicitly_wait(10)
brower.find_element_by_css_selector('[class="target"]').click()#点击下载图标
time.sleep(2)
shell=win32com.client.Dispatch("WScript.shell")
time.sleep(2)
shell.Sendkeys(r'G:\baidu.png'+'\n')
brower.quit()
