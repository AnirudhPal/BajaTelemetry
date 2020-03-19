# Import Libs
import serial

# Global Vars
serPort = serial.Serial(port = "/dev/ttyUSB0", baudrate = 9600)

# Loop
while True:
  print serPort.readline()
