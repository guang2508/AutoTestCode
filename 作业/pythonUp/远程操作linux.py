# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-04-01
import paramiko
ssh=paramiko.SSHClient()    #创建客户端ssh对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #设置连接方式
ssh.connect('192.168.0.102',22,'root','sdfsdf') #远程主机IP地址，端口号，用户名和密码
stdin,stdout,stderr=ssh.exec_command(
    '''ifconfig'''
)  #一次执行多条命令
print(str(stdout.read().decode("utf8")))

# sftp=ssh.open_sftp()    #将本地文件传送到远程机器
# sftp.put('')
ssh.close()