# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-08
import paramiko
import re
import time
#创建ssh对象
sshc=paramiko.SSHClient()
#设置连接方式
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ip地址，端口号，用户名，密码
sshc.connect("192.168.0.117",22,"root","sdfsdf")
#在连接的远程机器上执行命令,可执行多条，用 ; 隔开
while True:
    stdin,stdout,stderr=sshc.exec_command("cd /proc;head -4 meminfo")
    str=stdout.read().decode("utf8")
    lists=str.replace(' ','').split('\n') #转换成列表['MemTotal:2523572kB', 'MemFree:1311676kB', 'Buffers:25664kB', 'Cached:426048kB', '']
    sum=0
    for i in range(1,len(lists)-1):
        num=int(re.sub("\D","",lists[i]))
        unit=re.sub("\d","",lists[i].split(':')[1])  #取单位
        if unit=='B':
            num=int(num/1024)
        if unit=='M':
            num=num*1024
        sum += num
    avaMen=int(sum/int((re.sub("\D","",lists[0])))*100)
    now=time.strftime("%Y%m%d_%H:%M:%S",time.localtime(time.time()))
    print(f'{now}  {avaMen}%')
    with open('./ret.txt','a') as f:
        f.write(f'{now}  {avaMen}%\n')
    time.sleep(5)
#关闭连接，释放资源
sshc.close()