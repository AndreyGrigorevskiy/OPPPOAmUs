#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import string

sock = socket.socket()
sock.connect(('localhost', 9090))
action = True
while action:
    sock.send(input().encode('utf-8'))
    data = sock.recv(1024)
    print(data)
    print('continue typing ?(Y\N)')
    x = input()
    if x == 'N' or x == 'n':
        break


sock.close()
