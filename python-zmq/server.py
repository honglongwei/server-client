#coding=utf-8  

import zmq  
import time  
import commands
   
context = zmq.Context()  
socket = context.socket(zmq.REP)  
socket.bind("tcp://*:5555")  
   
while True:  
    #  Wait for next request from client  
    message = socket.recv()  
    print "Received request: ", message  
   
    #  Do some 'work'  
    cmd_ret = commands.getoutput(message)
   
    #  Send reply back to client  
    socket.send(cmd_ret)
