#!/usr/bin/python

import smbus
import math
import csv
import time
import sys
import datetime
import os

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

dlpf_set_addr = 0x1a
dlpf = 0x06

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

bus.write_byte_data(address, dlpf_set_addr, dlpf)

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

timestr = time.strftime("%Y-%m-%d_%H-%M-%S")

with open('/media/pi/3262-6564/Accel/'+timestr+'.csv', 'a') as f_output:
    w=csv.writer(f_output)
    w.writerow(['Time', 'X accel (g)', 'Y Accel (g)', 'Z accel (g)',
                'X Gyro (deg/s)', 'Y Gyro (deg/s)', 'Z Gyro (deg/s)',
                'X Rotation (deg)', 'Y Rotation (deg)'])
    
    while True:
        
        sec = time.time()
        meas_time = datetime.datetime.now()
        timestamp = meas_time.strftime("%H:%M:%S.%f")
        
        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)
        
        gyro_xout_scal = gyro_xout / 131
        gyro_yout_scal = gyro_yout / 131
        gyro_zout_scal = gyro_zout / 131
        
        xrot = get_x_rotation(gyro_xout,gyro_yout,gyro_zout)
        yrot = get_y_rotation(gyro_xout,gyro_yout,gyro_zout)

        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
               
        w.writerow([timestamp, accel_xout_scaled, accel_yout_scaled, accel_zout_scaled,
                    gyro_xout_scal, gyro_yout_scal, gyro_zout_scal,
                    xrot, yrot])
        
        delsec = time.time()-sec
        
        if (delsec < 0):
        
            delsec = 0
            
            if (0.05 - delsec < 0):
            
                delsec = 0.49 
            
            
        time.sleep(0.05 - delsec)
        
        
        
        
