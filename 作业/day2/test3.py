# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2

import subprocess

p = subprocess.Popen(
    "python ioTest.py",
    stdin=subprocess.PIPE, # 标准输入文件
    stdout=subprocess.PIPE,# 标准输出文件
    stderr=subprocess.PIPE,# 标准错误对象
    encoding="gbk"
)

inpList = ["1", "2", "3", "4"]

# 获取执行输出结果
out, err = p.communicate('\n'.join(inpList))


print("out =", out)
print("err =", err)

