# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-08
import paramiko
#创建ssh对象
sshc=paramiko.SSHClient()
#设置连接方式
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ip地址，端口号，用户名，密码
sshc.connect("192.168.0.117",22,"root","sdfsdf")


#在连接的远程机器上执行命令,可执行多条，用 ; 隔开
stdin,stdout,stderr=sshc.exec_command("cd /proc;dir")
ss=stdout.read().decode("utf8")
if 'tangjigaung' not in ss:
    stdin,stdout,stderr=sshc.exec_command("mkdir tangjiguang")

#帮助我们在远程主机和本地直接互相发送文件
sftp=sshc.open_sftp()
#把本地文件传到远程机器
sftp.put("G:\软件测试\作业\pythonUp\\memory.py","/proc/tangjiguang/memory.py")
#把远程机器的文件下载到本地
# sftp.get("远程主机上的路径","本地文件的路径")

#关闭连接，释放资源
sshc.close()
