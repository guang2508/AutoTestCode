# coding=utf8
from appium import webdriver
import time, traceback
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'g:\apk\com.ibox.calculators_3.1.0_1310.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    driver.implicitly_wait(10)
    driver.find_element_by_id("com.ibox.calculators:id/clear").click()
    time.sleep(1)
    driver.find_element_by_id("com.ibox.calculators:id/digit3").click()
    driver.find_element_by_id("com.ibox.calculators:id/plus").click()
    driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    time.sleep(1)
    driver.find_element_by_id("com.ibox.calculators:id/mul").click()
    driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
    driver.find_element_by_id("com.ibox.calculators:id/equal").click()
    time.sleep(1)
    result=driver.find_elements_by_class_name("android.widget.TextView")[1].text
    print(result)
    if result=='60':
        print("测试通过")
    else:
        print("测试不通过")
    pass
except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()

