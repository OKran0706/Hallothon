import serial
import time
a=0
ser = serial.Serial('COM4', 9600, timeout=1)
while True:
    print('iop')
    ser.write(b'd')
    time.sleep(2)
    a=a+1
    if a>1:
        break
    

ser.close()
