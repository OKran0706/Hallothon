import serial
import time
ser = serial.Serial('COM4', 9600, timeout=1)
while True:
    ser.write(b'w')
    time.sleep(1)
    break

ser.close()
