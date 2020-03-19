# Import Libs
import serial
from signal import signal, SIGINT
from sys import exit
import time

# Global Vars
OUT_FILE = "Data_"
ts = time.time()
fd = open(OUT_FILE + str(int(ts)) + ".csv", "w+")

# SIGINT Handler
def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or Ctrl-C received, Saving File')

    # Close File
    fd.close()
                
    # Terminate Prog            
    exit(0)

# Run Code
def run():
    # Register Handler
    signal(SIGINT, handler)

    # Open Serial
    serPort = serial.Serial(port = "/dev/ttyUSB0", baudrate = 9600)

    # Check Serial Open
    if(serPort.isOpen()):
        print('Serial open!')
    else:
        print('Serial didnt open!')
        exit(0)

    # CSV Header
    fd.write('Time Stamp, A0 Val, A1 Val, A2 Val, A3 Val, Accel X, Accel Y, Accel Z, Gyro X, Gyro Y, Gyro Z\n')

    # Infinite Loop
    while(True):
        # Get Serial Line
        line = serPort.readline()

        # Add Time Stamp
        ts = time.time()

        # Write to File
        fd.write(str(ts) + ", " + line[:-2] + '\n')

# Execute
run()
