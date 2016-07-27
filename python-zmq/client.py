#coding=utf-8  

import zmq  
   
context = zmq.Context()  
   
#  Socket to talk to server  
print "Connecting to server..."  
socket = context.socket(zmq.REQ)  
socket.connect ("tcp://0.0.0.0:5555")  
   
#  Do 10 requests, waiting each time for a response  
for request in range (1,10):  
    print "Sending request ", request,"..."  
    cmd = raw_input("Please input cmd:")
    socket.send (cmd)  
       
    #  Get the reply.  
    message = socket.recv()  
    print "Received reply ", request, "[", message, "]"
