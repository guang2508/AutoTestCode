# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-29
import os
import socket

sk=socket.socket()
sk.connect(("127.0.0.1",13000))

def post_file(sk_obj,path):
    """
    上传文件
    :param sk_obj:socket对象
    :param path: 文件路径
    :return: none
    """
    file_size=os.stat(path).st_size #获取文件大小
    sk_obj.sendall(str(file_size).encode("utf8"))   #发送文件大小
    sk_obj.recv(1024)   #避免粘包
    sk_obj.sendall(os.path.split(path)[1].encode("utf8"))  #发送文件名
    sk_obj.recv(1024)   #避免粘包
    with open(path,"rb") as f:
        while file_size>0:
            sk_obj.sendall(f.read(1024))
            file_size -= 1024

post_file(sk,"./123.png")
sk.close()