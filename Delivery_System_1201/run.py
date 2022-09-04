#-*- coding: utf-8 -*-
#@File    : run.py.py
#@Time    : 2021/11/21 9:33
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/21

print("----111----")
"""
设计流程：
    1- 把运行的模式与参数写在一个配置文件里
    2- 读取运行的配置文件的对应数据----yaml   ini
        -m shop_list
        --alluredir xxxxx
        -- excel筛选
    3- 使用pytest.main（[读取的运行模式]）
    
注意实现：
    代码里写了相对路径，基本上会报错  not found xxx文件
"""
