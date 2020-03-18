import os
import time

os.system("/home/pi/gps_start.sh")

time.sleep(10)

os.system("/home/pi/gps_end.sh")