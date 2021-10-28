import serial
import time
from datetime import datetime
import schedule
import os
import csv
import emailsend
def temp_check():
    


    def main_func():
        arduino = serial.Serial('com7', 9600)
        print('Established serial connection to Arduino')
        arduino_data = arduino.readline()

        decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split('\n')

        for item in list_values:
            list_in_floats.append(item)

        f1=open("2.txt","w")
        f1.write(str(datetime.now())+"  temperature: " +list_in_floats[0] +"\n")
        f1.close()
        emailsend.send_email()
        

        arduino_data = 0
        list_in_floats.clear()
        list_values.clear()
        arduino.close()
        

    # ----------------------------------------Main Code------------------------------------
    # Declare variables to be used
    list_values = []
    list_in_floats = []

    print('Program started')

    # Setting up the Arduino
    main_func()
    schedule.every(20).seconds.do(main_func)

    while True:
        schedule.run_pending()
        time.sleep(1)

temp_check()
        