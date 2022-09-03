# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/3/13


import requests


data = [
    {"action":"add_course", "data": '{"name":"课程01--xctext","desc":"01","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程02","desc":"02","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程03","desc":"03","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程04","desc":"04","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程05","desc":"05","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程06","desc":"06","display_idx":1}'},
]


# 一行代码实现接口请求，一次性传100个数据
sli = [requests.post(url="http://localhost/api/mgr/sq_mgr/", data=i) for i in data]


for res in sli:
    print(res.text)

