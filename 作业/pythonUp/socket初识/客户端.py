# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-29

import socket
sk=socket.socket()    #创建socket对象
sk.connect(("127.0.0.1",13000))
send_data=input(">>>")
sk.sendall(send_data.encode("utf8"))   #发送数据

server_data=sk.recv(1024).decode("utf8")   #接收到服务端数据
print("服务端：",server_data)

sk.close()  #释放资源