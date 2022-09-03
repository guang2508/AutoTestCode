# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-29
import os
import socket
sk=socket.socket()  #创建socket对象
sk.bind(("127.0.0.1",13000))    #绑定IP，端口
sk.listen() #开启监听
def get_file(sk_obj):
    """
    接收文件
    :param sk_obj:socket对象
    :return: none
    """
    file_size=int(sk_obj.recv(1024).decode("utf8"))
    sk_obj.sendall(b"ok")
    file_name=sk_obj.recv(1024).decode("utf8")
    sk_obj.sendall(b"ok")
    with open(f"./{file_name}","wb") as f:
        while file_size>0:
            f.write(sk_obj.recv(1024))
            file_size -= 1024
cnn,client_addr=sk.accept()
get_file(cnn)
cnn.close()
sk.close()
