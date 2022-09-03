# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-03-31

import socket
sk=socket.socket()
sk.connect(("127.0.0.1",13002))
while True:
    client_data=input("客：")
    sk.sendall(client_data.encode("utf8"))
    if client_data=='exit':break
    server_data=sk.recv(1024).decode("utf8")
    print(server_data)
sk.close()