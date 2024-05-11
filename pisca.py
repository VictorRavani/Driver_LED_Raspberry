
# Programa para piscar Led

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

while True:
    GPIO.output(21, 0)
    print (0)
    time.sleep(1)
    GPIO.output(21, 1)
    print (1)
    time.sleep(1)
    

