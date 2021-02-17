#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import string

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('test for my life'.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data)
