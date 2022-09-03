# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-01

import chardet
with open(r'G:\软件测试\作业要求\python进阶测试-作业1-字符编码集-task07\cfiles\gbk编码.txt','rb') as f1:
    data1=f1.read()
# print(chardet.detect(data1))
with open(r'G:\软件测试\作业要求\python进阶测试-作业1-字符编码集-task07\cfiles\utf8编码.txt','rb') as f2:
    data2=f2.read()
# print(chardet.detect(data2))
newData=data1.decode('gbk')+'\n'+data2.decode('utf8')
print(newData)
name=input('请输入 新文件的名称')
with open(f'G:/软件测试\作业要求/python进阶测试-作业1-字符编码集-task07/cfiles/{name}.txt','w',encoding='utf8') as f3:
    f3.write(newData)
