#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import string

sock = socket.socket()
sock.connect(('localhost', 9090))
action = True
print("to exit write to chat: /exit")
while action:
    message = input()
    if not message:
        message = " you are gay"
    if message == "/exit":
        break;
    message = message.encode('utf-8')
    sock.send(message)
    data = sock.recv(1024)
    print(data)

sock.close()
