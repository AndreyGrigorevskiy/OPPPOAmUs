#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket #библиотека сокета
import string #библиотека строк

print("сервер запущен")

sock = socket.socket() #создаем сокет
sock.bind(('',9090)) #инициализируем порт
sock.listen(1) #слушаем 1 это максимальное количество прослушиваний
conn, addr = sock.accept() #принримает подключение и выозвращяет новый сокет и адрес клиента

print('connected: ', addr)


#устанавливаем связь с клиентом и общяемся с ним
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(bytes.decode(data, encoding='utf-8'))
    conn.send(data.upper())

conn.close()

print("сервер остановлен")
