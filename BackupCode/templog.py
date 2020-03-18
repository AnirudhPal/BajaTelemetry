#!/usr/bin/python
import os
import time
import csv
import datetime
import sys
import RPi.GPIO as GPIO



#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(38, GPIO.OUT)

def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=",""))

timestr=time.strftime("%Y-%m-%d_%H-%M-%S")

with open('/media/pi/USEME/'+timestr+'.csv', 'a') as f_output:
    w=csv.writer(f_output)
    w.writerow(['Time (s)', 'Temp (C)'])
    t = 0
    
    while True:
        tempin = measure_temp()
        temp1=tempin[0:4]
        temp2=eval(temp1)
        w.writerow([t, temp2])
        print(temp2)
        print(t)
        t = t + 0.5
        time.sleep(0.5)
        
       # if temp2 >= 70:
       #     GPIO.output(38, 1)
            
       # if temp2 >= 80:
        #    GPIO.cleanup()
        #    exit()
            
            
        if t == 2700:
            GPIO.cleanup()
            exit()
            
            
        
        