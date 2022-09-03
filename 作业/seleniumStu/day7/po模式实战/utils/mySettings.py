# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : mySettings.py
# @ide     : PyCharm
# @time    : 2020/5/29 20:18

"""
配置文件
"""

# 域名，我们把网址配置成配置文件
DOMAIN = "http://127.0.0.1:8088"
# 超时时间
TIMEOUT = 10
# 轮询时间
POLL_FREQUENCY = 0.5
# driver 路径
driverPath = {
    "Chrome": "D:\\tool\selenium\chromedriver.exe",
    "Firefox": "D:\\tool\selenium\geodriver.exe"
}

# cookie，过期后需要更新的
cookieSli = [{'domain': '127.0.0.1',
              'httpOnly': False,
              'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
              'path': '/',
              'secure': False,
              'value': '1590754848'},
             {'domain': '127.0.0.1',
              # 'expiry': 1622290848,
              'httpOnly': False,
              'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
              'path': '/',
              'secure': False,
              'value': '1590754848'},
             {'domain': '127.0.0.1',
              # 'expiry': 1622290847.468446,
              'httpOnly': True,
              'name': 'beegosessionID',
              'path': '/',
              'secure': False,
              'value': '99de79817fc91d4100ba7c19cfb330f7'}]
