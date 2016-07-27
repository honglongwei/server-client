#! /usr/bin/env python
#-*- coding: utf-8 -*-

import socket

host='0.0.0.0'
port=50015

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host, port))
while 1:
    cmd = raw_input("Please input cmd:")
    s.sendall(cmd)
    data = s.recv(1024)
    print data
s.close()
