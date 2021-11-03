import zmq
import random
import sys
import os
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

pid = os.getpid()
count = 0
# print(pid)
while True:
    
    socket.send_string(str(pid))
    count+=1
    print(pid, count)
    time.sleep(30)