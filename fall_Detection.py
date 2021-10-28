import communication
import time
import socket, traceback

import string

host="<host ip>"

port=5555

def detect_fall():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.bind((host, port))
    b=0
    temp1=0
    tic=[]
    a=1
    while a==1:

        message, address = s.recvfrom(8192)

        #print(message)

        var1 = str(message)

        var2=var1.split(',')

        temp2=var2[2].strip(',')

        #print(temp2)

        temp3 = float(temp2)
        
        if (temp3>9):
            tic.append(time.perf_counter())
            toc= time.perf_counter()
            if toc-tic[0]>2:
                tic=[]
                b=0
            b+=1
            print(b)
            if(b>=12):
                print("Fall")
                a=0
                communication.communicate("call", "daughter")
                communication.communicate("call", "neighbour")
                exit()




