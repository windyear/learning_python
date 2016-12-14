#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
s=socket.socket()

s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\nHost: www.sina.com.cn\nConnection: keep-alive\n\n')

buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()

header,html = data.split(b'\n\n',1)
print(header.decode('utf-8'))

with open(r'D:\windyear_files\testfiles\sina_test.html','wb') as f:
    f.write(data)
