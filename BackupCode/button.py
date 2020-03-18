import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    input_state=GPIO.input(7)
        
    if input_state == True:
        print('Button is pressed')
        
    