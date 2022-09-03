# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-31

# import socket
# sk=socket.socket()
# sk.bind(("127.0.0.1",13001))
# sk.listen(5)
# while True:
#     cnn,addr=sk.accept()
#     while True:
#         try:
#             client_data=cnn.recv(1024)
#             if not client_data:raise Exception("收到空数据")
#         except:
#             print("意外中断")
#             break
#         if client_data.decode("utf8")=='exit':
#             break
#         print(client_data.decode("utf8"))
#         server_data=input("服：")
#         cnn.sendall(server_data.encode("utf8"))
#     cnn.close()
# sk.close()

import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人和女神搭讪了")
        while True:
            client_data=self.request.recv(1024).decode("utf8") #接收数据 类似cnn.recv(1024)
            print(client_data)
            if client_data=="exit":break
            server_data=input("服：")
            self.request.sendall(server_data.encode("utf8"))

server=socketserver.ThreadingTCPServer(("127.0.0.1",13002),Myserver)
print("女神上线了")
server.serve_forever() #服务端长连接