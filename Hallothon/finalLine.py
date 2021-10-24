import multiprocessing

from datetime import datetime

timenow = datetime.now()

current_time = timenow.strftime("%H:%M:%S")
print("Current Time =", current_time)
  

a=cv2.vc(1)
frame=0
start=1
if current_time==7:00:00 :
    detect=4
    morn=1

def action():
    if morn ==1:
    global move
        if morn
        speak(wake up)
        recognize face
        break
        speak(have a nice day)
        send(f)
        senf (f)
        start=1
    if morn==0:

def server():
    global value
    if value:
        detect=valde
        morn=0

def qr_det():
    global start,trigger,temp,frame,detect
    if frame!=0:
        a=dertect_qr()
        if a==detect:
            start=0
            action()
            start=1

def line_follow():
    global start,trigger,temp,frame
    while 1:
        v,frame=cv2.read
        bl_frame=cv2.blur(frame,(5,5))
        if start==1:

def print_cube(num):
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
  
    # both processes finished
    print("Done!")