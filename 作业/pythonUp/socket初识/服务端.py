# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-29

import socket
ip=("127.0.0.1",13000)  #配置服务器IP和端口号
sk=socket.socket()  #创建socket对象
sk.bind(ip)     #绑定IP和端口号
sk.listen()     #监听有没有请求过来
print("服务端已启动，正在监听请求")
cnn,addr=sk.accept()    #等待连接传入后，会返回一个新的套接字对象和客户端的IP地址、端口号
print("客户端的IP地址是：",addr)

client_data=cnn.recv(1024).decode("utf8")  #接收客户端消息
print("客户端：",client_data)

send_data=input(">>>")
cnn.sendall(send_data.encode("utf8"))  #发送数据

cnn.close() #释放资源
sk.close()