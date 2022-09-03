# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-22

# c="你好啊"
# d=c.encode("utf-8")     #编码
# print(d)
#
# e=b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x95\x8a'
# print(e.decode("utf-8"))    #解码，在编码的非交集部分，用utf-8编码就要用utf-8解码

# with open("./c.txt","w",encoding="utf-8") as f:   #用utf-8的编码形式写
#     f.write("键盘")
# with open("./c.txt","r",encoding="utf-8") as f:     #用utf-8的编码方式读
#     print(f.read())

# with open("./d.txt","wb") as f:
#     f.write("鼠标".encode("utf-8"))   #以wb二进制的方式打开文件，写入中文时需编码，不然会报错
# with open("./d.txt","rb") as f:
#     print(f.read().decode("utf-8"))     #文件写入的是二进制内容，读出的时候需要decode解码，不然读出的就是二进制数据

# import subprocess
# subprocess.check_output("mspaint")
# # print(out.decode("gbk"))
# print("aaf")

# import os
# os.system("mspaint")
# print("ass")

# from subprocess import Popen,PIPE    #PIPE--管道
# child=Popen("ping www.taobao.com -a",stdout=PIPE,shell=False)
# output,err=child.communicate()       #communicate---执行Popen里的
# print(output.decode("GBK"))
# print(err)

import time
def show_time(func):
    def inner(case_name):
        beginTime=time.time()
        func(case_name)
        end_time=time.time()
        print("总耗时：",end_time-beginTime)
    return inner

@show_time
def foo(case_name):
    print("这种",case_name)
    time.sleep(1)
foo(11)