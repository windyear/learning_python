#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
s=socket.socket()
s.connect(('127.0.0.1',1234))
#accept the message of welcome
print(s.recv(1024).decode('utf-8'))
for data in [b'Windyear',b'Wolf',b'Ying']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()