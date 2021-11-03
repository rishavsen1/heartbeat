import zmq
import time
import os
import signal
from subprocess import Popen
import shutil

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.setsockopt(zmq.RCVTIMEO, 90000)
socket.setsockopt(zmq.LINGER, 0)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while(True):

    try :
        msg = socket.recv()
        print(msg)
    except:
        try:
            os.kill(int(msg), signal.SIGTERM)
        except:
            continue
        finally:
            time.sleep(1)
            # locate = shutil.which(worker.py)  #if on PATH
            Popen("python C:/Program/heartbeat/worker.py")
            time.sleep(1)
    