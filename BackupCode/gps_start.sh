sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

sleep 01

sudo gpspipe -r -d -l -o /media/pi/01CB-2ADA5/GPS/$(date +"%F_%H-%M-%S").nmea


