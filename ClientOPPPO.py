#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import string

sock = socket.socket()
sock.connect(('localhost', 9090))
i = 0
while i<10:
    sock.send(input().encode('utf-8'))
    data = sock.recv(1024)
    print(data)
    i += 1

sock.close()
